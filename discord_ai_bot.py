import logging
import discord
import openai
from discord.ext import commands


DISCORD_BOT_TOKEN = "DISCORD_BOT_TOKEN"
OPENAI_API_KEY = "OPENAI_API_KEY"

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)
openai.api_key = OPENAI_API_KEY
conversation_history = []

logging.basicConfig(level=logging.INFO)

async def generate_image(prompt):
    try:
        response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
        print(response)
        return response['data'][0]['url']
    except Exception as e:
        logging.error(f"Error generating image: {e}")
        return "Sorry, an error occurred while generating the image."

async def generate_text(prompt):
    try:
        prompt_copy = conversation_history
        prompt_copy.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompt_copy)
        message = response["choices"][0]["message"]["content"].strip()
        conversation_history.append({"role": "assistant", "content": message})
        print(message)
        return message
    except Exception as e:
        logging.error(f"Error generating text: {e}")
        return "Sorry, an error occurred while generating the text."

@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user}")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@client.tree.command(name="commands")
async def commands(interaction: discord.Interaction):
    commands = "/chat <prompt>\n/image <prompt>"
    await interaction.response.send_message(commands)

@client.tree.command(name="image")
async def image(interaction: discord.Interaction, *, prompt:str):
    logging.info(f"User image prompt '{prompt}'")
    await interaction.response.defer()
    generated_image = await generate_image(prompt)
    print(generate_image)    
    await interaction.followup.send(generated_image)

@client.tree.command(name="chat")
async def chat(interaction: discord.Interaction, *, prompt: str):
    logging.info(f"User text prompt '{prompt}'")
    await interaction.response.defer()
    generated_text = await generate_text(prompt)
    await interaction.followup.send(generated_text)

client.run(DISCORD_BOT_TOKEN)   

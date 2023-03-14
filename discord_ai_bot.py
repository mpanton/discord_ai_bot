import logging
import discord
import openai
from discord.ext import commands


DISCORD_BOT_TOKEN = "discord bot token here"
OPENAI_API_KEY = "openai api key here"

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)
openai.api_key = OPENAI_API_KEY
conversation_history = []

logging.basicConfig(level=logging.INFO)

async def generate_image(prompt):
    try:
        response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
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
        return message
    except Exception as e:
        logging.error(f"Error generating text: {e}")
        return "Sorry, an error occurred while generating the text."

@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user}")

@client.command()
async def commands(ctx):
    commands = "chat <followed by a question etc>\nimage <followed by keywords>"
    await ctx.send(commands)

@client.command()
async def image(ctx, *, prompt):
    logging.info(f"User image prompt '{prompt}'")
    generated_image = await generate_image(prompt)
    await ctx.send(generated_image)

@client.command()
async def chat(ctx, *, prompt):
    logging.info(f"User text prompt '{prompt}'")
    generated_text = await generate_text(prompt)
    await ctx.send(generated_text)

client.run(DISCORD_BOT_TOKEN)

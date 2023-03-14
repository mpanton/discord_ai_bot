Discord Chatbot using OpenAI's GPT-3
------------------------------------

This is a simple Discord chatbot that uses OpenAI's GPT-3 to generate responses to user inputs. The bot is capable of generating both text and images based on user prompts.

### Requirements

-   A Discord account
-   A Discord bot token (can be obtained from the Discord Developer Portal)
-   OpenAI API key
-   Python 3.7 or higher

### Installation

1.  Clone the repository to your local machine using `git clone https://github.com/mpanton/discord_ai_chatbot.git`
2.  Navigate to the project directory and install the necessary dependencies using `pip install -r requirements.txt`
3.  Fill in the required values in the `discord_ai_bot` file (DISCORD_BOT_TOKEN and OPENAI_API_KEY)

### Usage

1.  Invite the bot to your Discord server using the OAuth2 URL generated from the Discord Developer Portal.
2.  Run the bot using `python discord_ai_bot.py`
3.  Use the `@botname chat` command to start a chat with the bot.
4.  Use the `@botname image` command followed by keywords to generate an image based on the keywords.

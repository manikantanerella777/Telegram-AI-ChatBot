# Telegram-AI-ChatBot
🚀 Meet Your AI Chatbot! 🤖  
Your smart assistant on Telegram! This AI-powered chatbot can: 
✅ Answer questions instantly 
✅ Help with daily tasks &amp; reminders 
✅ Generate text, summaries, and ideas 
✅ Provide entertainment &amp; fun facts 
✅ Chat naturally &amp; engage in conversations  Just send a message and let the AI do the rest! Try it now. 🎉

# Create Your Own ChatGPT on Telegram: A Step-by-Step Guide to Building a Python-powered AI Bot

## Introduction

Are you tired of using the same AI-powered chatbots available on the market? Do you want to build your own chatbot and customize it to your liking? Then, look no further! In this blog post, we'll walk you through a step-by-step guide on creating your very own AI bot using Python, Telegram, and OpenAI GPT models. Get ready to unleash the power of artificial intelligence right at your fingertips!

when you change models at conf.py be sure start new evctordb since vector dimension is different for each model.

## Router  usage

you can give any llm in routes.py file.

You can add any additional llm to the routes.py file. 

![telegramgpt_llm_router](https://github.com/user-attachments/assets/ff5af371-d23b-408f-981f-678f5ad5ac50)




## Quick start

### Prerequisites

- A Telegram account
- A Telegram bot API token (you can get one from the BotFather bot on Telegram)
- An OpenAI API key (you can get one by signing up on the OpenAI website)
- make sure you added your username env file
- Docker and docker-compose

### Steps

1. Clone the repository:

```bash
git clone --recursive https://github.com/emingenc/telegramGPT.git
cd telegramGPT
```

2. Set up environment variables create .env file
    
    ```bash
    TELEGRAM_TOKEN="your telegram token"
    OPENAI_API_KEY="your openai api key"
    BOTNAME="your bots name"
    TAVILY_API_KEY="tav api key"
    USERS=allowed users
    ANTHROPIC_API_KEY="anthropic api key"

    ```

3. Run the bot using docker-compose:
    
    ```bash
    docker-compose up
    ```



## Step 1: Setting up your Telegram bot

Before diving into the code, you'll need to create a new bot on Telegram. Follow these simple steps:

1. Open the Telegram app and search for the "BotFather" bot.
2. Start a chat with BotFather and send the command "/newbot" to create a new bot.
3. Choose a name and username for your bot. BotFather will provide you with a unique API token, which you'll need later. Save it somewhere safe.

## Step 2: Cloning the code repository

Clone the code repository from GitHub using the following command:

```bash
Congratulations! You've just built your own chatbot using Python, Telegram, and OpenAI GPT models. Now you can enjoy the power of AI through a personalized, engaging chat experience on Telegram. Don't forget to share your thoughts and experiences in the comments below. Happy coding!

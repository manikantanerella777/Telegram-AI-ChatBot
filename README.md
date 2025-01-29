# Telegram AI Chatbot

This project demonstrates how to create a Telegram bot that uses OpenAI GPT models and Gemini API for AI-powered interactions, with MongoDB for data storage and Docker for deployment.
"AI-powered chatbot using Telegram, OpenAI, and Gemini"

🚀 Meet Your AI Chatbot! 🤖
```bash
✅ Answer questions instantly
✅ Help with daily tasks & reminders
✅ Generate text, summaries, and ideas
✅ Provide entertainment & fun facts 
✅ Chat naturally & engage in conversations  
Just send a message and let the AI do the rest! Try it now. 🎉
```

## Features

1. **User Registration**: Stores user details (first name, username, phone number) in MongoDB.
2. **Gemini-Powered Chat**: Uses Gemini API (via OpenAI) to respond to user queries.
3. **Image/File Analysis**: Accepts images/files (JPG, PNG, PDF) and uses Gemini for content analysis.
4. **Web Search**: Users can search the web using the /websearch command.

# Prerequisites

- Telegram bot token
- OpenAI API key
- MongoDB instance
- Docker and Docker Compose
## 1. Create a GitHub Repository
- Go to GitHub.
- Click New in the upper-right corner to create a new repository.
- Name the repository (e.g., telegram-ai-chatbot).
- Optionally, add a README.md and choose a license (e.g., MIT).
- Click Create repository.
## 2. Set Up Your Project Locally
Clone the repository and set up your project files on your local machine:

```bash
git clone https://github.com/your-username/telegram-ai-chatbot.git
cd telegram-ai-chatbot
```
## 3. Project Directory Structure
Create the following structure for your project:
Add Your Project Files or File Structure
Make sure your project folder contains these files:-

```bash
Telegram-AI-ChatBot/
│
├── bot.py                  # Main bot logic
├── routes.py               # Custom routes for different tasks (like web search)
├── conf.py                 # Configuration file for keys and settings
├── requirements.txt        # Required Python libraries
├── .env                    # Environment variables (API keys, etc.)
├── Dockerfile              # Docker setup for the bot
├── docker-compose.yml      # Docker Compose for container orchestration
├── models/                 # Directory for any custom models or agents (if needed)
│   └── researcher.py       # For research or web search agents
└── README.md               # Project documentation
```

## 4.Initialize Git in Your Project Folder
- Open Terminal / Command Prompt and navigate to your project folder:
```bash
cd path/to/your/project
```
- Initialize Git:
```bash
git init
```
- Add the GitHub repository as a remote origin (replace your-username and repo-name):
```bash
git remote add origin https://github.com/your-username/Telegram-AI-ChatBo
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 📌 Create Your Own AI Chatbot on Telegram
This guide will walk you through building a Python-powered AI chatbot using Telegram, OpenAI, and Gemini models. Customize your bot, integrate AI capabilities, and deploy it efficiently!

## ⚡ Features
### 1️⃣ User Registration
Stores first name, username, and chat_id in MongoDB upon first interaction.
Uses Telegram’s contact button to request and store the phone number.
Sends a confirmation message after successful registration.
### 2️⃣ AI-Powered Chat (Gemini & OpenAI)
Uses Google’s Gemini API (google.generativeai) for AI-powered conversations.
Supports multi-LLM routing (e.g., OpenAI, Anthropic) in routes.py.
Stores full chat history (user input + bot response) in MongoDB with timestamps.
### 3️⃣ Image & File Analysis
Accepts images (JPG, PNG) and PDFs.
Uses Gemini AI to analyze and describe their content.
Saves file metadata (filename, description, etc.) in MongoDB.
### 4️⃣ Web Search Integration
Users can perform a web search by typing /websearch.
The bot fetches an AI-generated summary along with top web links.
## 🚀 Quick Start Guide
### 🔹 Prerequisites
A Telegram account
A Telegram Bot API token (from BotFather)
An OpenAI API key (Get it here)
A Google Gemini API key (Get it here)
Docker & docker-compose installed
### 🔹 Setup & Installation
#### 1️⃣ Clone the Repository
```bash
git clone --recursive https://github.com/your-username/Telegram-AI-ChatBot.git
cd Telegram-AI-ChatBot
```

#### 2️⃣ Set Up Environment Variables
Create a .env file and add your API keys:

```bash
TELEGRAM_TOKEN="your_telegram_bot_token"
OPENAI_API_KEY="your_openai_api_key"
BOTNAME="your_bot_name"
TAVILY_API_KEY="your_tavily_api_key"
USERS="allowed_users"
ANTHROPIC_API_KEY="your_anthropic_api_key"
```
#### 3️⃣ Run the Bot with Docker
```bash
docker-compose up
```
🎉 Congratulations! Your AI chatbot is now live on Telegram!

Configuration Guide
🔹 Model Selection
Define your LLM (Large Language Model) in routes.py.
Supports OpenAI, Gemini, and Anthropic models.
If changing models in conf.py, ensure you restart the vector database (as dimensions vary per model).
🔹 Database Setup
Uses MongoDB to store user data, chat history, and file metadata.
Ensure MongoDB is running before starting the bot.
📸Screenshot & Usage


Step 1: Setting up your Telegram bot
Before diving into the code, you'll need to create a new bot on Telegram. Follow these simple steps:

Open the Telegram app and search for the "BotFather" bot.
Start a chat with BotFather and send the command "/newbot" to create a new bot.
Choose a name and username for your bot. BotFather will provide you with a unique API token, which you'll need later. Save it somewhere safe.
Step 2: Cloning the code repository
Clone the code repository from GitHub using the following command:

bash
Copy
Edit
git clone --recursive https://github.com/emingenc/telegramGPT.git
cd telegramGPT
Step 3: Installing the dependencies
Install the required dependencies using the following command:

bash
Copy
Edit
pip3 install -r requirements.txt
Step 4: Exploring the code
In our project, we have four main files:

telegram_bot.py: The main script that handles the Telegram bot's functionality.
gpt_message_handler.py: Contains functions for interacting with OpenAI's GPT models and managing chat history.
conf.py: A configuration file to store the list of allowed users.
requirements.txt: Lists the required Python libraries for the project.
Step 5: Configuring the bot
Edit conf.py to add the usernames of users allowed to interact with your bot. For example:

python
Copy
Edit
users = ["your_telegram_username"]
Step 6: Setting up the environment variables
You need to set up environment variables: TELEGRAM_TOKEN (the API token you received from BotFather) and OPENAI_API_KEY (your OpenAI API key). BOTNAME (name of bot) You can either add them to your system's environment variables or use a .env file.

Step 7: Running the bot
Start your bot by running the telegram_bot.py script:

bash
Copy
Edit
python3 telegram_bot.py
Your bot is now up and running! Start a chat with your Telegram bot and see it in action.

Conclusion
Congratulations! You've just built your own chatbot using Python, Telegram, and OpenAI GPT models. Now you can enjoy the power of AI through a personalized, engaging chat experience on Telegram. Don't forget to share your thoughts and experiences in the comments below. Happy coding!

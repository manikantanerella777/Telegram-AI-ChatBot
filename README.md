# Telegram AI Chatbot

This project demonstrates how to create a Telegram bot that uses OpenAI GPT models and Gemini API for AI-powered interactions, with MongoDB for data storage and Docker for deployment.

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

```bash
telegram-ai-chatbot/
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
## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telegram-ai-chatbot.git
   cd telegram-ai-chatbot
```

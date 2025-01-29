# Telegram AI Chatbot

This project demonstrates how to create a Telegram bot that uses OpenAI GPT models and Gemini API for AI-powered interactions, with MongoDB for data storage and Docker for deployment.

## Features

1. **User Registration**: Stores user details (first name, username, phone number) in MongoDB.
2. **Gemini-Powered Chat**: Uses Gemini API (via OpenAI) to respond to user queries.
3. **Image/File Analysis**: Accepts images/files (JPG, PNG, PDF) and uses Gemini for content analysis.
4. **Web Search**: Users can search the web using the /websearch command.

## Prerequisites

- Telegram bot token
- OpenAI API key
- MongoDB instance
- Docker and Docker Compose

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telegram-ai-chatbot.git
   cd telegram-ai-chatbot
```
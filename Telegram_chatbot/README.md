# Telegram Chatbot - Step by Step Guide

A comprehensive Telegram bot built with aiogram 3.x framework, featuring multiple commands, keyboard buttons, and optional OpenAI integration.

## 📋 Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Bot](#running-the-bot)
6. [Bot Commands](#bot-commands)
7. [Code Structure](#code-structure)
8. [Troubleshooting](#troubleshooting)

## ✨ Features

- ✅ Multiple command handlers (`/start`, `/help`, `/info`, `/echo`, etc.)
- ✅ Reply keyboard buttons for easy interaction
- ✅ Inline keyboard buttons with callbacks
- ✅ State management (FSM) for multi-step interactions
- ✅ Echo functionality
- ✅ Random number generator
- ✅ Optional OpenAI integration for AI chat
- ✅ Error handling and logging
- ✅ Startup/shutdown handlers

## 🔧 Prerequisites

- Python 3.8 or higher
- A Telegram account
- (Optional) OpenAI API key for AI features

## 📦 Installation

### Step 1: Clone or Download the Project

```bash
cd Telegram_chatbot
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Step 1: Get Your Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Create `.env` File

Create a `.env` file in the project root:

```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here  # Optional
```

**Note:** The `.env.example` file shows the format. Copy it to `.env` and fill in your values.

### Step 3: (Optional) Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Add it to your `.env` file

## 🚀 Running the Bot

### Start the Bot

```bash
python echo_bot.py
```

You should see:
```
INFO - Bot started successfully!
```

### Test Your Bot

1. Open Telegram
2. Search for your bot (the username you gave it)
3. Send `/start` command
4. You should see a welcome message with keyboard buttons!

## 📱 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and show welcome message |
| `/help` | Show help message with all commands |
| `/info` | Show bot and user information |
| `/echo <text>` | Echo your message back |
| `/keyboard` | Show keyboard buttons |
| `/cancel` | Cancel current operation |

## 🎮 Keyboard Buttons

The bot includes several keyboard buttons:

- **📝 Echo Message** - Echo a message you send
- **ℹ️ Info** - Show bot information
- **🎲 Random Number** - Generate a random number (1-100)
- **🤖 AI Chat** - Chat with AI (requires OpenAI API key)
- **❌ Cancel** - Cancel current operation

## 📚 Code Structure

The bot code is organized into 15 clear steps:

1. **Imports** - All required libraries
2. **Logging Configuration** - Set up logging
3. **Environment Variables** - Load configuration
4. **Bot Initialization** - Create bot and dispatcher
5. **State Definitions** - FSM states for user interactions
6. **Keyboard Markups** - Create reply and inline keyboards
7. **Command Handlers** - Handle `/start`, `/help`, etc.
8. **Message Handlers** - Handle text messages and buttons
9. **AI Integration** - OpenAI chat functionality
10. **General Message Handler** - Fallback for all messages
11. **Callback Handlers** - Handle inline button clicks
12. **Error Handler** - Handle errors gracefully
13. **Startup/Shutdown** - Bot lifecycle handlers
14. **Main Function** - Start polling
15. **Entry Point** - Run the bot

## 🔍 Understanding Each Step

### Step 1: Imports
```python
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
```
- Import necessary classes and functions from aiogram

### Step 2: Logging
```python
logging.basicConfig(level=logging.INFO)
```
- Configure logging to track bot activity

### Step 3: Environment Variables
```python
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
```
- Load sensitive data from `.env` file

### Step 4: Bot Initialization
```python
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(storage=storage)
```
- Create bot instance and dispatcher

### Step 5: States
```python
class UserStates(StatesGroup):
    waiting_for_echo = State()
```
- Define states for multi-step interactions

### Step 6: Keyboards
```python
def get_main_keyboard() -> ReplyKeyboardMarkup:
    # Create keyboard buttons
```
- Create interactive keyboards

### Step 7-15: Handlers
- Each handler function processes specific events
- Decorators (`@dp.message()`) register handlers
- Async functions handle asynchronous operations

## 🐛 Troubleshooting

### Bot Not Responding

1. **Check Token**: Verify `TELEGRAM_TOKEN` in `.env` is correct
2. **Check Internet**: Ensure you have internet connection
3. **Check Logs**: Look for error messages in console
4. **Restart Bot**: Stop (Ctrl+C) and restart the bot

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### OpenAI Not Working

1. Check `OPENAI_API_KEY` in `.env`
2. Verify API key is valid
3. Check your OpenAI account balance
4. Bot will work without OpenAI (AI features disabled)

### Module Not Found

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install missing package
pip install <package_name>
```

## 📝 Example Usage

1. **Start Bot**: `/start`
2. **Get Info**: Click "ℹ️ Info" button or `/info`
3. **Echo Message**: Click "📝 Echo Message", then send a message
4. **Random Number**: Click "🎲 Random Number"
5. **AI Chat**: Click "🤖 AI Chat", then send a message (requires OpenAI)

## 🔐 Security Notes

- Never commit `.env` file to version control
- Keep your bot token secret
- Don't share your OpenAI API key
- Use environment variables for sensitive data

## 📖 Learn More

- [aiogram Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contributing

Feel free to add more features:
- Database integration
- Webhook support
- More commands
- File handling
- Image processing

## 📄 License

This project is open source and available for educational purposes.

---

**Happy Bot Building! 🤖**




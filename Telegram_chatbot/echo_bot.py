import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Get token from environment
Telegram_token = os.getenv("TELEGRAM_TOKEN")
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")


# Basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Bot")

# Initialize the Bot and Dispatcher
bot = Bot(token=Telegram_token)
dp = Dispatcher()

# Configure OpenAI if available
openai.api_key = "OPENAI_API_KEY"
logger.info("OpenAI API configured")


# Handler for /start command
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    """ Handler for /start command """
    await message.answer(f"Hello! I'm your Telegram bot.")
    welcome_text = (
        f"👋 Hello, {message.from_user.first_name}!\n\n"
        f"Welcome to the Telegram Chatbot!\n\n"
        f"📋 Available commands:\n"
        f"/start - Start the bot\n"
        f"/help - Show help message\n"
        f"/info - Show bot information\n"
        f"/echo <text> - Echo your message\n"
        f"/keyboard - Show keyboard buttons\n\n"
        f"Or use the buttons below! 👇"
    )
    
    await message.answer(welcome_text)
    logger.info(f"User {message.from_user.id} started the bot")

# Help command
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Handler for /help command"""
    help_text = (
        "📚 Bot Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/info - Show bot information\n"
        "/echo <text> - Echo your message back\n"
        "/keyboard - Show keyboard buttons\n"
        "/cancel - Cancel current operation\n\n"
        "💡 Tip: You can also use the keyboard buttons!"
    )
    await message.answer(help_text)


# Info handler
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    """Handler for /info command"""
    user_info = (
        f"ℹ️ Bot Information\n\n"
        f"👤 Your ID: {message.from_user.id}\n"
        f"📛 Your Name: {message.from_user.first_name}\n"
        f"🆔 Username: @{message.from_user.username or 'N/A'}\n"
        f"💬 Chat ID: {message.chat.id}\n"
        f"🤖 Bot Framework: aiogram 3.x\n"
        f"🔧 OpenAI: {'✅ Enabled' if  OPEN_API_KEY else '❌ Disabled'}"
    )
    await message.answer(user_info)


@dp.message(Command("echo"))
async def cmd_echo(message: types.Message):
    """Handler for /echo command"""
    # Get text after /echo command
    text = message.text.split("/echo", 1)[1].strip()
    
    if not text:
        await message.answer("❌ Please provide text to echo!\nUsage: /echo <your text>")
        return
    
    await message.answer(f"📢 Echo: {text}")

async def main():
    # Start polling
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())


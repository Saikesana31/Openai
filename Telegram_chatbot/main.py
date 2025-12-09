from random import choices
from dotenv import load_dotenv
import os
import logging
import asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
import openai
import sys

load_dotenv()

#Load telegram and openai token
Telegram_token = os.getenv("TELEGRAM_TOKEN")
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPEN_API_KEY

# Basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Bot")

# store previous response
class Reference:
    '''
    A class to store previously response from openai api    '''
    def __init__(self) -> None:
        self.response  = ""

reference = Reference()
model_name = "gpt-3.5-turbo-0125"


#install bot and dispatcher
bot = Bot(token=Telegram_token)
dp = Dispatcher()

#clear the past rsponse
def clear_past():
    reference.response = ""


# Handlers
@dp.message(Command('start'))
async def cmd_start_main(message:types.Message):
    await message.answer(f'hii i am tele bot created by sai.How can i assist you?')

    logger.info(f"User {message.from_user.id} started the bot")

@dp.message(Command('help'))
async def cmd_help_main(message:types.Message):
    '''This helper handler '''
    help_command = """
    Hi,
    /start - to start
    /clear - to clear past
    /help - to get help menu
    i hope this help u
    """
    await message.answer(help_command)

# clear handler
@dp.message(Command('clear'))
async def cmd_clear(message:types.Message):
    clear_past()
    await message.answer("i have cleared the past conversations")


#open ai handler
@dp.message()
async def chatgpt(message : types.Message):
    '''
    A handler to process the user input and generate a response using GPT api
    '''
    response = openai.ChatCompletion.create(
        model = model_name,
        messages = [
            {"role":"assistant","content": reference.response}, #role assistant
            {"role":"user","content": message.text} # our Query
        ]
    )

    reference.response = response['choices'][0]['message']['content']
    await bot.send_message(chat_id = message.chat.id,text = reference.response)


















# start polling
async def main():
    await dp.start_polling(bot,skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())


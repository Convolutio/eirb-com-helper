import asyncio
from argparse import ArgumentParser

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv_vault import load_dotenv

from os import getenv

import sys

load_dotenv()

bot_token = getenv("BOT_TOKEN")
chat_id = getenv("CHAT_ID")

async def send_message(msg):
    async with Bot(
        token=bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.MARKDOWN_V2,
        ),
    ) as bot:
        await bot.send_message(chat_id=chat_id, text=msg)

if __name__ == "__main__":
    message = sys.stdin.read()
    asyncio.run(send_message(message))


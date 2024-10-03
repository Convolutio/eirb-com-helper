from aiogram import Bot
from aiogram.client.default import DefaultBotProperties, Default
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest

from dotenv_vault import load_dotenv

from os import getenv

class BadMessageFormatException(Exception):
    """
    Exception Raised if the given message is wrongly formatted for Telegram 
    """
    pass

load_dotenv()

bot_token = getenv("BOT_TOKEN")
default_chat_id = getenv("CHAT_ID", default=None)


async def send_message(msg: str, chat_id: str | None = None, html_format=False):
    if chat_id is None:
        chat_id = default_chat_id
    async with Bot(
        token=bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.MARKDOWN_V2,
        ),
    ) as bot:
        try :
            await bot.send_message(chat_id=chat_id, text=msg,
                                   parse_mode = ParseMode.HTML if html_format else Default('parse_mode')
                                   )
        except TelegramBadRequest as e :
            raise BadMessageFormatException(f"The given message is wrongly formatted: {e}")

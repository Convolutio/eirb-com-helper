from aiogram import Bot
from aiogram.client.default import DefaultBotProperties, Default
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from sulguk import AiogramSulgukMiddleware, SULGUK_PARSE_MODE
from .converter import htmlToSulgukHtml, markdownToMarkdownV2

from os import getenv

bot_token = getenv("BOT_TOKEN")
default_chat_id = getenv("CHAT_ID", default=None)

class BadMessageFormatException(Exception):
    """
    Exception Raised if the given message is wrongly formatted for Telegram 
    """
    pass


async def send_message(msg: str, chat_id: str | None = None, html_format=False):
    """
    send the given message in private message, with applying it a range of parsing for telegram to correctly format it
    """
    if chat_id is None:
        chat_id = default_chat_id
    async with Bot(
        token=bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.MARKDOWN_V2,
        ),
    ) as bot:
        try :
            if html_format:
                bot.session.middleware(AiogramSulgukMiddleware())
                msg = htmlToSulgukHtml(msg)
                await bot.send_message(
                        chat_id=chat_id, text=msg,
                        parse_mode=SULGUK_PARSE_MODE
                        )
            else:
                msg = markdownToMarkdownV2(msg)
                await bot.send_message(chat_id=chat_id, text=msg)
        except TelegramBadRequest as e :
            raise BadMessageFormatException(f"The given message is wrongly formatted: {e}")

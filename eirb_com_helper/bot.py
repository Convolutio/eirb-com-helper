from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties, Default
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.formatting import Text, Code

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

dp = Dispatcher()

@dp.message(CommandStart())
async def echo_chat_id_handler(message: Message) -> None:
    """
    Handler will send to the sender the chat id
    """
    await message.answer(Text("Hello! You're chat id is :", Code(str(message.chat.id))))


async def init_bot() -> Bot:
    return Bot(
        token=bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.MARKDOWN_V2,
        )
    )

async def launch_listening(bot: Bot):
    print("\t Start Bot...")
    await dp.start_polling(bot)


async def send_message(bot: Bot, msg: str, chat_id: str | None = None, html_format=False):
    if chat_id is None:
        chat_id = default_chat_id
    try :
        await bot.send_message(chat_id=chat_id, text=msg,
                                parse_mode = ParseMode.HTML if html_format else Default('parse_mode')
                                )
    except TelegramBadRequest as e :
        raise BadMessageFormatException(f"The given message is wrongly formatted: {e}")

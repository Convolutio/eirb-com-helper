import asyncio
import sys

from dotenv_vault import load_dotenv
load_dotenv()

from eirb_com_helper.bot import send_message

if __name__ == "__main__":
    message = sys.stdin.read()
    asyncio.run(send_message(message))

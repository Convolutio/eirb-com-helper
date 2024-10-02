import asyncio
import sys
from eirb_com_helper.bot import send_message

if __name__ == "__main__":
    message = sys.stdin.read()
    asyncio.run(send_message(message))

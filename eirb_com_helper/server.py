from flask import Flask, request, abort
import asyncio
from .bot import send_message as bot_send_message, BadMessageFormatException
from .converter import toMarkdownV2, htmlToMarkdown

APP_NAME = "TELEGRAM_FILE_SENDER"

app = Flask(APP_NAME)

@app.post("/send")
def send_message():
    mime_type = request.content_type
    is_markdown_content: bool = False
    if mime_type.startswith("text/plain"):
        is_markdown_content = True
    elif not mime_type.startswith("text/html"):
        abort(401, "bad given body mime type")

    print(type(request.data))
    converter = toMarkdownV2 if is_markdown_content else (lambda m: toMarkdownV2(htmlToMarkdown(m))) 
    msg = request.data.decode()
    try:
        asyncio.run(bot_send_message(converter(msg)))
    except BadMessageFormatException as e:
        abort(401, str(e))
    return "Message sent!\n", 200

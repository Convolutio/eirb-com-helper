from flask import Flask, request, abort
from flask_cors import CORS
import asyncio
from .bot import send_message as bot_send_message, BadMessageFormatException
from .converter import toMarkdownV2, htmlToMarkdown

APP_NAME = "TELEGRAM_FILE_SENDER"

app = Flask(APP_NAME)
CORS(app)

@app.post("/send")
def send_message():
    """
    Expected request body: application/json
        * chat_id : str
        * content_type : "html" | "markdown" 
        * content : str
    """
    if not request.is_json:
        abort(401, "wrong given body mime type")

    data = request.json
    content_type = data['content_type']
    msg = data['content']
    chat_id = data['chat_id']

    is_markdown_content: bool = False
    if content_type == "markdown":
        is_markdown_content = True
    elif content_type != "html":
        abort(401, "`content_type` field must match \"html\" or \"markdown\" values")

    if msg is None:
        abort(401, "missing `content` field")
    if not isinstance(msg, str):
        abort(401, "wrong given `content` field's type")
    if chat_id is None:
        abort(401, "missing `chat_id` field")

    converter = toMarkdownV2 if is_markdown_content else (lambda m: toMarkdownV2(htmlToMarkdown(m))) 
    try:
        asyncio.run(bot_send_message(converter(msg), chat_id))
    except BadMessageFormatException as e:
        abort(401, str(e))
    return "Message sent!\n", 200

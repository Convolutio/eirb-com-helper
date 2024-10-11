from flask import Flask, request, abort, render_template
from flask_cors import CORS
import bleach
import asyncio
from .bot import send_message as bot_send_message, BadMessageFormatException

APP_NAME = "TELEGRAM_FILE_SENDER"
ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS.union({"u", "s", "del", "pre", "p", "br", "span"}) # cf telegram supported tags + bleach allowed_tags
ALLOWED_ATTRIBUTES = dict(bleach.sanitizer.ALLOWED_ATTRIBUTES)
ALLOWED_ATTRIBUTES['span'] = ['class']
ALLOWED_ATTRIBUTES['code'] = ['class']

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
    msg = bleach.clean(data['content'], tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
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

    try:
        asyncio.run(bot_send_message(msg, chat_id, not is_markdown_content))
    except BadMessageFormatException as e:
        abort(401, str(e))
    return "Message sent!\n", 200


# Converter

## Install dependencies

```sh
poetry install
```

Add the token of the sender bot in the `./.env` file.  
Also add your chat id where the bot has to send messages in this file.

```env
BOT_TOKEN="your_telegram_bot_token"
```

### How to get these credentials

For the bot token, talk to @FatherBot.

For the chat id, chat in private with the Bot and then go to `https://api.telegram.org/bot<BOT-TOKEN>/getUpdates`.


## Use the server

### Start it

```sh
# from the repository's source
poetry shell
python main.py
```

### Endpoints

#### `POST` `/send`

Requires the `"Content-Type": "application/json"` header with a json body with the following structure
```json
{
    "chat_id": "the id of your chat with the bot",
    "content_type": "markdown",
    "content": "Your *beautiful* markdown message with a **standard** `format`."
}
```

or

```json
{
    "chat_id": "the id of your chat with the bot",
    "content_type": "html",
    "content": "Your <em>beautiful</em> message with the <code>HTML</code> <strong>format</strong>."
}
```

Send the given message in the channel with the set up chat id.

## Use the server since a frontend interface

```sh
cd frontend
python -m http.server 8080
```

Then go to `localhost:8080` in your browser.

## Test the server

TODO

## Run command-line tools

Also precise your chat id in the `.env` file
```
CHAT_ID="your chat id"
```

### Convert Markdown input into MarkdownV2

```sh
# from the repository's source
poetry shell
cat your_markdown_file.md | python convert.py
```

### Convert HTML input into MarkdownV2

*Not supported yet.*

```sh
# from the repository's source
poetry shell
cat your_html_message.html | python convert.py --html
```

### Send MarkdownV2 message in private

```sh
# from the repository's source
poetry shell
cat your_markdownV2_file.md | python send_message.py
```

### Do all in one!

Just pipe !

```sh
# from the repository's source
poetry shell
cat your_markdown_file.md | python convert.py | python send_message.py
```

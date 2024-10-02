# Converter

## Install dependencies

```sh
poetry install
```

Add the token of the sender bot in the `./.env` file.  
Also add your chat id where the bot has to send messages in this file.

```env
BOT_TOKEN="your_telegram_bot_token"
CHAT_ID="your_chat_id"
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

Requires a body among:
    - `text/plain`: a message content written with the standard markdown syntax
    - `text/html`: a message content written with html tags

Send the given message in the channel with the set up chat id.

## Test the server

Run it then try the curl requests in `eirb-com-helper/tests/test_request.sh`

## Run command-line tools

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

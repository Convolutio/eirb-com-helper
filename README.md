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


## Convert Markdown input into MarkdownV2

```sh
# from the repository's source
poetry shell
cat your_markdown_file.md | python eirb-com-helper/converter.py
```

## Send MarkdownV2 message in private

```sh
# from the repository's source
poetry shell
cat your_markdownV2_file.md | python eirb-com-helper/bot.py
```

## Do all in one!

Just pipe !

```sh
# from the repository's source
poetry shell
cat your_markdown_file.md | python eirb-com-helper/converter.py | python eirb-com-helper/bot.py
```

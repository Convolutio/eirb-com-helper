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

## Use the server

### Start the chat id giver

Run this listen server for the bot to give to each user in private message their chat id when they run the command `/start` in this channel.

```sh
poetry shell
poetry run python listenChatId.py
```

### Start the well-formatted message sender

Run in another process this Flask server, which will be listened by default on `http://127.0.0.1:5000`

```sh
# from the repository's source
poetry shell
python main.py
```

TODO
- [ ]: instanciate once the Bot in the Flask app

### Endpoints

#### `POST` `/send`

Requires the `"Content-Type": "application/json"` header with a json body with the following structure
```json
{
    "chat_id": "the id of your chat with the bot",
    "content_type": "markdown",
    "content": "Your _beautiful_ markdown message with a strict `format`."
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

### About the format

#### Markdown

The markdown is strict. Then, the syntax here is supported

```md
# Title
## Subtitle
### Subsubtitle
#### Subsubsubtitle
'\_', '\*', '\[', '\]', '\(', '\)', '\~', '\`', '\>', '\#', '\+', '\-', '\=', '\|', '\{', '\}', '\.', '\!'
_ , * , [ , ] , ( , ) , ~ , ` , > , # , + , - , = , | , { , } , . , !
We will remove the \ symbol from the original text.
**bold text**
*bold text*
_italic text_
__underline__
~no valid strikethrough~
~~strikethrough~~
||spoiler||
*bold _italic bold ~~italic bold strikethrough ||italic bold strikethrough spoiler||~~ __underline italic bold___ bold*
__underline italic bold__
[link](https://www.google.com)
- [ ] Uncompleted task list item
- [x] Completed task list item
> Quote

> Multiline Quote In Markdown it's not possible to send multiline quote in telegram without using code block or html tag but telegramify_markdown can do it.

> If you quote is too long, it will be automatically set in expandable citation. 
> This is the second line of the quote.
> This is the third line of the quote.
> This is the fourth line of the quote.
> This is the fifth line of the quote.

```python
print("Hello, World!")
```
This is `inline code`
1. First ordered list item
2. Another item
    - Unordered sub-list.
    - Another item.
1. Actual numbers don't matter, just that it's a number
```

#### HTML

Use `<span class="spoiler"/></span>` for the spoiler.


## Run the frontend interface

```sh
python -m http.server 8080 -d frontend
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

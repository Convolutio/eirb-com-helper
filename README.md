# Converter

## Install dependencies

```sh
poetry install
```

Add the token and the username of the sender bot in the `./.env` file. The
username is for displaying purpose.
In CLI mode, also add your chat id where the bot has to send messages in this
file.

```env
BOT_TOKEN="your_telegram_bot_token"
BOT_USERNAME="@YourBotUsername"

# Optional
CHAT_ID="your_chat_id"
```

### How to get these credentials

For the bot token, talk to @FatherBot. For the chat id, you can run the chat id
giver then in the chat with the bot, run the `/start` command.

## Use the server

### With docker compose

Run `docker-compose up`, or `docker compose up`, to run the bot using docker.

### Without docker compose

Simply run `./run.sh`, to run the server and the telegram listener separatly,
refer to the next two sections.

### Start the chat id giver

Run this listen server for the bot to give to each user in private message
their chat id when they run the command `/start` in this channel.

```sh
# from the repository's source
poetry shell
python listenChatId.py
```

### Start the well-formatted message sender

Run in another process this Flask server, which will be listened by default on `http://127.0.0.1:5000`

```sh
# from the repository's source
poetry shell
python main.py
```

### Endpoints

#### `POST` `/send`

Requires the `"Content-Type": "application/json"` header with a json body with
the following structure

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

#### `GET` `/`

Render a frontend interface to input the markdown, render it in HTML and then
send the message as in the previewed html.

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

\`\`\`python
print("Hello, World!")
\`\`\`
This is `inline code`
1. First ordered list item
2. Another item
    - Unordered sub-list.
    - Another item.
1. Actual numbers don't matter, just that it's a number
```

#### HTML

Use `<span class="spoiler"/></span>` for the spoiler.

The frontend interface use the rendered HTML to request from the flask server a
message sending. It is more tolerant with the markdown syntax and more
transparent with the final got message in telegram.

## Test the server

TODO

## Run command-line tools

Also precise your chat id in the `.env` file

```sh
CHAT_ID="your chat id"
```

### Convert Markdown input into MarkdownV2

```sh
# from the repository's source
poetry shell
cat your_markdown_file.md | python convert.py
```

### Convert HTML input into MarkdownV2

*Not supported yet and not useful, as telegram already supports some html.*

```sh
# from the repository's source
poetry shell
cat your_html_message.html | python convert.py --html
```

### Send Markdown message in private

The conversion into MarkdownV2 is embedded into the module.

```sh
# from the repository's source
poetry shell
cat your_markdown_file.md | python send_message.py
```

### Send HTML message in private

*Not supported yet.*

```sh
# from the repository's source
poetry shell
cat your_html_message.html | python send_message.py --html
```

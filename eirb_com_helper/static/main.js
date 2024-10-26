// Main elements
const markdownContentTextArea = document.getElementById("message");
const renderedContentDiv = document.getElementById("rendered-content");
const chatIdInput = document.getElementById("chat-id");
const submitButton = document.getElementById("submit-button");
const dataForm = document.getElementById("dataForm");

// Help modal
const helpButton = document.getElementById("help-button");
const helpModal = document.getElementById("help-modal");
const helpModalClose = document.getElementById("help-modal--close");
const helpModalBack = document.getElementById("help-modal--back");

// Preview
const previewButton = document.getElementById("preview-button");
const previewButtonPreview = document.getElementById("preview-button--preview");
const previewButtonNopreview = document.getElementById("preview-button--nopreview");

const defaultText = `
Enter your message here

> The previewed message will be sent to you by \`{{ bot_username }}\`. Contact him in private on Telegram, next run the \`/start\` command to get your chat id. Then, fill the field below with this chat id and click on *Submit* to get the message in your private Telegram chat.

Below you can get some samples of markdown syntax :

**bold \*\*text**
__bold \_\_text__

*italic \*text*
_italic \_text_
<u>underline</u>
~strikethrough~
~~strikethrough~~
||spoiler||
**bold _italic bold ~~italic bold strikethrough ||italic bold strikethrough spoiler||~~ <u>underline italic bold_</u> bold**
[inline URL](http://www.example.com/)
👍
\`inline fixed-width code\`
\`\`\`
pre-formatted fixed-width code block
\`\`\`
\`\`\`python
pre-formatted fixed-width code block written in the Python programming language
\`\`\`
>Block quotation started
>Block quotation continued
>Block quotation continued
>Block quotation continued
>The last line of the block quotation

- [ ] not done
- [x] done
`;

// Init inputs
const draft = getDraft();
if (draft !== "")
  markdownContentTextArea.value = draft;

chatIdInput.value = getChatId();
renderContent(markdownContentTextArea.value, renderedContentDiv);

helpButton.addEventListener("click", () => {
  helpModal.classList.remove("hidden");
});

helpModalClose.addEventListener("click", () => {
  helpModal.classList.add("hidden");
});

helpModalBack.addEventListener("click", () => {
  helpModal.classList.add("hidden");
});

listenForRender(markdownContentTextArea, renderedContentDiv);
listenForSubmit(
  submitButton,
  markdownContentTextArea,
  chatIdInput,
  renderedContentDiv
);

// Preview Button interaction
previewButton.addEventListener("click", () => {
  renderedContentDiv.classList.toggle("show");
  previewButtonPreview.classList.toggle("hidden");
  previewButtonNopreview.classList.toggle("hidden");
});


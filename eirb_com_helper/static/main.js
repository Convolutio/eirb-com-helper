const markdownContentTextArea = document.getElementById("message");
const renderedContentDiv = document.getElementById("rendered-content");
const chatIdInput = document.getElementById("chat-id");
const submitButton = document.getElementById("submit-button");
const dataForm = document.getElementById("dataForm");

listenForRender(markdownContentTextArea, renderedContentDiv);
listenForSubmit(submitButton, markdownContentTextArea, chatIdInput, renderedContentDiv);

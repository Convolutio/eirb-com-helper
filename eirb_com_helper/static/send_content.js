function sendFile(msg, chat_id) {
  fetch("/send", {
    method: 'POST',
    headers: { 'Content-Type' : 'application/json' },
    body: JSON.stringify({ chat_id, content_type: "html", content: msg })
  })
    .then(response => {
      if (response.ok)
        response.text().then(resMessage => {
          alert("Ok: " + resMessage);
        });
      else
        throw new Error('The message have not been sent. Please edit your input.');
    })
    .catch(err => alert(err));
}

function listenForSubmit(submitButton, markdownContentTextArea, chatIdInput, renderedContentDiv) {
  dataForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const msg = renderedContentDiv.innerHTML;
      const chat_id = chatIdInput.value;
      sendFile(msg, chat_id);
    });

  function updateButtonState() {
    submitButton.disabled = chatIdInput.value.length === 0
      || markdownContentTextArea.value.length === 0;
  }
  chatIdInput.addEventListener("input", () => {
    updateButtonState();
    setChatId(chatIdInput.value);
  });
  markdownContentTextArea.addEventListener("input", updateButtonState);

  updateButtonState();
}

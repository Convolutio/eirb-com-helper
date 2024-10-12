function sendFile(msg, chat_id) {
  fetch("/send", {
    method: 'POST',
    headers: { 'Content-Type' : 'application/json' },
    body: JSON.stringify({ chat_id, content_type: "html", content: msg })
  })
    .then(
      () => { console.log("The message has been well sent!"); }
    );
}

document.getElementById("dataForm")
  .addEventListener('submit', (e) => {
    e.preventDefault();
    const msg = document.getElementById("rendered-content").innerHTML;
    const chat_id = document.getElementById("chat-id").value
    sendFile(msg, chat_id);
  });

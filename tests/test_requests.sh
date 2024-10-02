curl -X POST -H "Content-Type: text/plain" -d "$(cat msg.md)" 127.0.0.1:5000/send
curl -X POST -H "Content-Type: text/html" -d "$(cat msg.html)" 127.0.0.1:5000/send

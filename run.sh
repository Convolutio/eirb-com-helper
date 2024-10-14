#!/bin/sh

poetry run python main.py &
poetry run python listenChatId.py

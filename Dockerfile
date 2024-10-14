FROM alpine:3.20

RUN apk add python3 poetry

COPY . .

RUN poetry install

CMD ["./run.sh"]

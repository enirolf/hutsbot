FROM python:3.8-alpine as develop

WORKDIR /app

RUN apk add bash gcc musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN pip install tox

COPY ./run_bot.sh /app/run_bot.sh
RUN chmod +x run_bot.sh

FROM develop as production

COPY .env /app
COPY bot/config.py /app
COPY bot/hutsbot.py /app

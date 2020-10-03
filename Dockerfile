FROM python:3.8-alpine as develop

WORKDIR /app

RUN apk add bash gcc musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN pip install tox
COPY tox.ini /app

COPY ./run_bot.sh /app/run_bot.sh
RUN chmod +x run_bot.sh

COPY test /app/test

FROM develop as production

COPY bot /app/bot

FROM python:3.8-alpine as develop

WORKDIR /app

RUN apk add bash gcc musl-dev

ENV CONSUMER_KEY=$CONSUMER_KEY
ENV CONSUMER_SECRET=$CONSUMER_SECRET
ENV ACCESS_TOKEN=$ACCESS_TOKEN
ENV ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET

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

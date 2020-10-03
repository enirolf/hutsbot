#!/bin/sh

ssh -i ./deploy_key florine@$SERVER_IP
docker pull $DOCKER_IMAGE:latest
docker run -d $DOCKER_IMAGE:latest ./run_bot.sh

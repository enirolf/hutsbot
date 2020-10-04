#!/bin/sh
eval "$(ssh-agent -s)"
chmod 600 /tmp/deploy_key
ssh-add /tmp/deploy_key

ssh -i /tmp/deploy_key git@$SERVER_IP pwd -o StrictHostKeyChecking=no
docker pull $DOCKER_IMAGE:latest
docker run -d $DOCKER_IMAGE:latest ./run_bot.sh

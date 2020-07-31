#!/bin/bash
VERSION=`cat version`
UPDATE_DAY=`cat update`
IMAGE_NAME="pp-bot:${VERSION}"
CONTAINER="pp-bot"

docker build -t  ${IMAGE_NAME} .
docker run -dit --rm \
  -e VERSION=${VERSION} \
  -e UPDATE_DAY=${UPDATE_DAY} \
  --env-file envfile.txt \
  --name ${CONTAINER} \
  ${IMAGE_NAME}

#!/bin/bash

VERSION=`cat version`
IMAGE_NAME="pp-bot:${VERSION}"
CONTAINER="pp-bot"

docker stop ${CONTAINER}
docker build -t ${IMAGE_NAME} .
docker run -dit --rm \
  -e VERSION=${VERSION} \
  -e UPDATE_DAY=${UPDATE_DAY} \
  -v `pwd`/images:/images \
  --env-file envfile.txt \
  --name ${CONTAINER} \
  ${IMAGE_NAME}

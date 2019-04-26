#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push fkynjyq/interview_schedule.web:$TRAVIS_BRANCH
docker push fkynjyq/interview_schedule.docs:$TRAVIS_BRANCH
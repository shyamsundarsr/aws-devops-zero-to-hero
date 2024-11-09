#!/bin/bash
set -e

# Stop the running container (if any)
echo "Stopping docker containers"
containerID='docker ps | awk -F" " '{Print $1}'
docker rm -f $containerID

#!/bin/bash
set -e

# Stop the running container (if any)
echo "Stopping docker containers"
containerID=$(docker ps | awk 'NR>1 {print $1}')
docker rm -f $containerID

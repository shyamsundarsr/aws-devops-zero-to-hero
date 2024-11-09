#!/bin/bash
set -e

# Stop the running container (if any)
echo "Stopping docker containers"
containerID=$(sudo docker ps -q)
sudo docker rm -f $containerID
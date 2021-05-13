#!/bin/bash

# Exit in case of error
set -e

# Get script path
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
BASE_DIR="$(dirname "$SCRIPTPATH")"

set -a
source "$BASE_DIR/.env.qa"
set +a

ANSIBLE_PATH="$BASE_DIR/deployment/ansible/playbook/files"
echo "Creating file in $ANSIBLE_PATH"

docker-compose -f docker-compose.yml config > "$ANSIBLE_PATH/docker-stack.yml"

# docker-auto-labels docker-stack.yml

# docker stack deploy -c docker-stack.yml --with-registry-auth pizzaparlor

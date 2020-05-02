#!/bin/bash

echo "Creating Backup"
docker-compose exec -T database /usr/bin/pg_dump --data-only -U postgres -d postgres > backup.sql
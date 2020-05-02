#!/usr/bin/env bash

__dir__="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "--== Seeding the database ==--"
flask init-db
flask create-user admin
flask create-user david

echo "--== Running development server ==--"
flask run --host 0.0.0.0

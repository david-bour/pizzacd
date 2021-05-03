#!/bin/bash

__dir__="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "$FLASK_APP_CONFIG" = "Production" ]]; then
    echo "--== Setting up Production Environment ==--"
    gunicorn pizza:app
else
    echo "--== Setting up Development Environment ==--"
    echo "--== Seeding the database ==--"
    flask db upgrade
    flask create-user admin
    flask create-user david
    echo "--== Running development server ==--"
    flask run --host 0.0.0.0
fi

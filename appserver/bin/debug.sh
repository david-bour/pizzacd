#!/bin/bash
flask db upgrade && \
flask create-user admin && \
flask create-user david && \
pip install debugpy -t /tmp && python /tmp/debugpy --wait-for-client --listen 0.0.0.0:5678 -m flask run --no-debugger --host 0.0.0.0 --port 5000
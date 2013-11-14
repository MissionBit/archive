#!/bin/bash

PID=$(ps -ef | grep 'server.py' | grep -v grep | awk '{ print $2 }')

if [ -n "$PID" ]; then
    echo "killing process with PID: $PID"
    kill $PID
fi

echo "Starting server..."
nohup python -u server.py > server.log 2>&1 &

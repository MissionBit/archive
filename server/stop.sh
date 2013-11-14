#!/bin/bash

PID=$(ps -f -u $USER | grep 'server.py' | grep -v grep | awk '{ print $2 }')

if [ -n "$PID" ]; then
    echo "killing process with PID: $PID"
    kill $PID
fi

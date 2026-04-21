#!/bin/bash
./pyenv/bin/pip install -r ./requirements.txt 
while true; do
    timeout 7200 ./pyenv/bin/python ./run.py
    echo "Restarting after 2 hrs to clear threads."
    sleep 2
done
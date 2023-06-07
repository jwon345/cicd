# Testing Webhooks

## What is this?
This project has webhooks linked to send a post request when a push is sent. 
     currently linked to my personal server :)

## .service file

    [Unit]
    Description=CiCd pipeline testing

    [Service]
    Type=simple
    ExecStartPre=/bin/bash /home/james/Dev/cicd/gitUpdate.sh
    ExecStart=/usr/bin/python3 /home/james/Dev/cicd/server.py
    WorkingDirectory=/home/james/Dev/cicd
    Restart=always
    RestartSec=5
    StartLimitInterval=60s
    StartLimitBurst=3
    User=james

    [Install]
    WantedBy=default.target


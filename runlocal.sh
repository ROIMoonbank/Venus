#!/bin/bash
# Updated 2025-05-22

sudo pip3 install -r requirements.txt
gunicorn -b :8080 main:app

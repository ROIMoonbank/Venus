#!/bin/bash
# Updated 2025-06-05

sudo pip3 install -r requirements.txt
gunicorn --bind 0.0.0.0:8080 main:app

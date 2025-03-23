#!/bin/bash

echo "Starting Flask application..."
gunicorn --bind 0.0.0.0:5000 app:app

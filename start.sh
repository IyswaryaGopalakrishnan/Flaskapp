#!/bin/bash

echo "Starting Flask application..."
gunicorn -w 4 -b 0.0.0.0:$PORT app:app


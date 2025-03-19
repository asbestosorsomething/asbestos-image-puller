import os
from flask import Flask, send_file, request
import logging
from datetime import datetime
import json

with open('config.json') as f:
    d = json.load(f)

# Create a Flask application
app = Flask(__name__)

# Log setup
log_file = f"{d['logfile']}"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(message)s")

# Path to your image file
IMAGE_PATH = f"{d['imagefile']}"  # Update with your image's file path

# Route to serve the image
@app.route("/image")
def serve_image():
    # Log the IP address of the person accessing the image
    ip_address = request.remote_addr
    log_access(ip_address)
    
    # Serve the image file
    return send_file(IMAGE_PATH)

# Function to log the IP address and timestamp
def log_access(ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"{timestamp} - IP: {ip}")

# Run the Flask app
if __name__ == "__main__":
    app.run(host=f"{d['server']}", port=8080)  # Accessible on your local network or externally if you configure port forwarding
# asbestosorsomething on github
# shoutout to SYM!

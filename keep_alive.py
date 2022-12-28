from flask import Flask, render_template
from threading import Thread

app = Flask('')
@app.route('/')

def main():
  return "J.Cole bot is live."

def run():
  app.run(host="0.0.0.0", port=8080)

def _keep_alive():
    server = Thread(target=run)
    server.start()
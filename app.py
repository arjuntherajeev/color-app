import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "pink": "#be2edd",
    "yellow": "#ffff00",
    "white": "#ffffff",
    "purple": "#7d3c98"
}

@app.route("/")
def main():
    color = random.choice(["red","green","yellow"])
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route("/test")
def test():
    return "TEST!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

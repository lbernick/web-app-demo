from flask import Flask, jsonify
from .animals import NOISES, speak

app = Flask(__name__)


@app.route("/animals")
def animals():
    return jsonify(list(NOISES.keys()))


@app.route("/animals/<animal>")
def make_noise(animal):
    return speak(animal)


@app.route("/statusz")
def statusz():
    return "All systems go!"


@app.route("/")
def index():
    return "Hello World"

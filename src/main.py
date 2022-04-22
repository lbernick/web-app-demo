from flask import Flask, flash, request, render_template
from .animals import speak

app = Flask(__name__)


@app.route("/statusz")
def statusz():
    return "<p>All systems go!</p>"


@app.route("/")
def index():
    return render_template("index.html")

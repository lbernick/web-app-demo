from flask import Flask, jsonify
import os
from redis import Redis
from .animals import NOISES, speak

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", 6379)
redis = Redis(host=redis_host, port=redis_port)

@app.route("/animals")
def animals():
    return jsonify(list(NOISES.keys()))


@app.route("/animals/<animal>")
def make_noise(animal):
    return speak(animal)


@app.route("/hits")
def get_hit_count():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return counter


@app.route("/statusz")
def statusz():
    return "All systems go!"


@app.route("/")
def index():
    return "Hello World!"

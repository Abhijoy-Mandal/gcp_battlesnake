import logging
import os
import typing

from flask import Flask
from flask import request
from main import *

app = Flask("Battlesnake")

@app.get("/")
def on_info():
    return info()

@app.post("/start")
def on_start():
    game_state = request.get_json()
    start(game_state)
    return "ok"

@app.post("/move")
def on_move():
    game_state = request.get_json()
    return move(game_state)

@app.post("/end")
def on_end():
    game_state = request.get_json()
    end(game_state)
    return "ok"

@app.after_request
def identify_server(response):
    response.headers.set(
        "server", "gcp"
    )
    return response


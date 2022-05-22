from flask import render_template, request
from app import app
from models.player import *
from models.player_list import *


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/", methods=["POST"])
def player1():
    player_1_name = request.form["player1_name"]
    player_1_choice = request.form["player1_choice"]
    player_1 = Player(player_1_name, player_1_choice)
    player_2_name = request.form["player2_name"]
    player_2_choice = request.form["player2_choice"]

    player_2 = Player(player_2_name, player_2_choice)

    add_player(player_1)
    add_player(player_2)
    winner = decide_winner(player_1, player_2)
    return render_template(
        "result.html",
        title="Result",
        winner=winner,
        player_1=player_1,
        player_2=player_2,
    )

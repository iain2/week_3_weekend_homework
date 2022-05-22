from models.player import *

player_list = []


def add_player(player):
    player_list.append(player)


def decide_winner(player1, player2):
    if player1.choice == "Rock" and player2.choice == "Scissors":
        return player1.name
    elif player1.choice == "Rock" and player2.choice == "Paper":
        return player2.name
    elif player1.choice == "Rock" and player2.choice == "Rock":
        return
    elif player1.choice == "Paper" and player2.choice == "Paper":
        return
    elif player1.choice == "Paper" and player2.choice == "Rock":
        return player1.name
    elif player1.choice == "Paper" and player2.choice == "Scissors":
        return player2.name
    elif player1.choice == "Scissors" and player2.choice == "Paper":
        return player1.name
    elif player1.choice == "Scissors" and player2.choice == "Rock":
        return player2.name
    elif player1.choice == "Scissors" and player2.choice == "Scissors":
        return

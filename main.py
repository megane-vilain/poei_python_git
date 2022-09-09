import random
import sys
import os
from flask import Flask, render_template, request, send_file, redirect, url_for, Response


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Menu():
    return render_template('home.html')

def create_player(name, pv, force, armure):
    return [name, pv, force, armure]

@app.route('/play_game', methods=['GET', 'POST'])
def play_game():
    if request.method == 'POST':
        nb_monsters_killed = 0
        player_name = request.form.get['player']
        player = create_player(player_name, 50, 5, 5)
        while player[1] > 0:
            start_combat(player)
            if(player[1] > 0):
                nb_monsters_killed = nb_monsters_killed + 1
        return render_template("play.html", nb_monster=str(nb_monsters_killed))        
    return render_template("play.html")

def create_monster():
    monster_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    monster_name = random.choice(monster_names)
    return generate_monster(monster_name)

def generate_monster(mosnster_name):
    return [mosnster_name, random.randint(5,20), random.randint(3,8), random.randint(0,5)]


def start_combat(player):
    monster = create_monster()
    player
    while player[1] > 0 and monster[1] > 0:
        monster[1] = handle_damage(monster[1], monster[2], player[2])
        if(monster[1] > 0):
            player[1] = handle_damage(player[1], player[2], monster[2])         
    return player         

def handle_damage(pv, armure, attack):
    if(attack > armure):
        return pv - (attack - armure)
    else: 
        return pv - 1

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
from crypt import methods
from distutils.log import debug
import random
import sys
import os
from flask import flask, render_template, request, send_file, redirect, url_for, Response


app = flask(__name__)

@app.rote('/', methods=['GET', 'POST'])

def Menu():
    return render_template('home.hyml')
def create_player(name, pv, force, armure):
    return [name, pv, force, armure]


def create_monster():
    monster_name = input('Choose a name for the next opponent: ')
    return generate_monster(monster_name)

def generate_monster(monster_name):
    return [monster_name, random.randint(5,20), random.randint(3,8), random.randint(0,5)]


def start_combat(player):
    monster = create_monster()
    player
    while player[1] > 0 and monster[1] > 0:
        monster[1] = handle_damage(monster[1], monster[2], player[2])
        print('Le joueur', player[0], 'attaque le monstre', monster[0])
        print('Il lui reste', monster[1], 'pv')

        if(monster[1] > 0):
            player[1] = handle_damage(player[1], player[2], monster[2])
            print('Le monstre attque le joueur', player[0])
            print('Il reste ', player[1], 'pv')
    if(player[1] > 0):
        print('Le joeur', player[0], 'a battu le monstre', monster[0])  
        print('Il lui reste', player[1], 'pv')        
                
    return player         

def handle_damage(pv, armure, attack):
    if(attack > armure):
        return pv - (attack - armure)
    else: 
        return pv - 1

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
    nb_monsters_killed = 0
    play = True
    while play:
        player_name = input("Choisissez un pseudo pour votre personnage : ")
        player = create_player(player_name, 50, 5, 5)
        while player[1] > 0:
            start_combat(player)
            if(player[1] > 0):
                nb_monsters_killed = nb_monsters_killed + 1

        print('Le joueur', player_name, 'est décedé après avoir tué', nb_monsters_killed, 'monstres')
        play_again = input("Aimez vous le jeu ? o/n] : ")
    
        while play_again.upper() != "O" and play_again.upper() != "N":
            
            play_again = input("Aimez vous le jeu ? [o/n] : ")
        
        if (play_again.upper() != "O"):
            play = False
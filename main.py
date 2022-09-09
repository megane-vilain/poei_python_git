import random
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Menu():
    return render_template('home.html')

def create_player(name, pv, force, armure):
    return [name, pv, force, armure]

@app.route('/play_game', methods=['GET', 'POST'])
def play_game():
    if request.method == 'POST':
        monster_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        monster_slain = []
        nb_monsters_killed = 0
        player_name = request.form.get('player')
        player = create_player(player_name, 50, 5, 5)
        while player[1] > 0:
            monster_name = random.choice(monster_names)
            start_combat(player, monster_name)
            if(player[1] > 0):
                nb_monsters_killed = nb_monsters_killed + 1
                monster_slain.append(monster_name)
        return render_template("play.html", player=player_name, nb_monster=str(nb_monsters_killed), monster_list = monster_slain)        
    return render_template("play.html")

def generate_monster(mosnster_name):
    return [mosnster_name, random.randint(5,20), random.randint(3,8), random.randint(0,5)]


def start_combat(player, monster_name):
    monster = generate_monster(monster_name)
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
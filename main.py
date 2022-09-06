from random import random

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
    return player         

def handle_damage(pv, armure, attack):
    if(attack > armure):
        return pv - (attack - armure)
    else: 
        return pv - 1

if __name__ == '__main__':
    player = create_player('Megane', 50, 5, 5)
    print('Welcome to the game', player[0])    


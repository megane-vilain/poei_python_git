from random import random


import random

def create_monster():
    monster_name = input('Choose a name for the next opponent: ')
    monster =  generate_monster(monster_name)
    return monster

def generate_monster(monster_name):
    return [monster_name, random.randint(5,20), random.randint(3,8), random.randint(0,5)]


if __name__ == '__main__':
    print('Welcome to the game!')
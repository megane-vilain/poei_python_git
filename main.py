def create_player(name, pv, force, armure):
    return [name, pv, force, armure]

if __name__ == '__main__':
    player = create_player('Megane', 50, 5, 5)
    print('Welcome to the game', player[0])    


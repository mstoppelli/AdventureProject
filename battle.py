import characters, player

def do_battle(player, enemy):
    while enemy.is_alive():
        action = input('What would you like to do?')
        if action == 'attack':
            raise NotImplementedError
        elif action == 'defend':
            raise NotImplementedError
        
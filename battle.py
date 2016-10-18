from utilities import *
from time import *


def input_action():
    action = input('What would you like to do?')
    actions = ['attack', 'defend', 'flee', 'item']
    if action in actions:
        return action
    else:
        print('Please input a valid action.')
        return input_action()


def battle(player, enemy):
    print('You are fighting a {}'.format(enemy))
    while player.is_alive() and enemy.is_alive():
        clear()
        print('Player HP:', player.print_health())
        print('Enemy HP:', enemy.print_health())
        action = input_action()
        if action == 'attack':
            clear()
            player.attack(enemy)
            sleep(2)
        elif action == 'defend':
            raise NotImplementedError
        elif action == 'item':
            raise NotImplementedError
        elif action == 'item':
            raise NotImplementedError
        enemy.attack(player)
        sleep(2)
    if player.hp > 0:
        msg = 'You stand victorious! the {} is defeated.'.format(enemy.name)
        msg = formatText(msg, 'GREEN')
        print(msg)
    elif enemy.hp > 0:
        msg = 'You have been defeated!'
        msg = formatText(msg, 'RED')
        print(msg)

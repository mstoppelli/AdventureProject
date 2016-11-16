from utilities import *
import copy
from time import sleep


def input_action():
    action = input('What would you like to do?')
    actions = ['attack', 'defend', 'flee', 'item', 'debug kill']
    if action in actions:
        return action
    else:
        print('Please input a valid action.')
        return input_action()


def battle(player, enemy):
    e = copy.copy(enemy)
    while player.is_alive() and e.is_alive():
        clear()
        print('{} HP:'.format(player.name), player.print_health())
        print('{} HP:'.format(e.name), e.print_health())
        action = input_action()
        if action == 'attack':
            clear()
            player.attack(e)
            sleep(2)
        elif action == 'defend':
            raise NotImplementedError
        elif action == 'item':
            raise NotImplementedError
        elif action == 'item':
            raise NotImplementedError
        elif action == 'debug kill':
            e.hp = 0
        e.attack(player)
        sleep(2)
    if player.hp > 0:
        msg = 'You stand victorious! the {} is defeated.'.format(e.name)
        msg = formatText(msg, 'GREEN')
        print(msg)
        sleep(3)
    elif e.hp > 0:
        msg = 'You have been defeated!'
        msg = formatText(msg, 'RED')
        print(msg)
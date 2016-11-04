from utilities import *
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
    while player.is_alive() and enemy.is_alive():
        clear()
        print('{} HP:'.format(player.name), player.print_health())
        print('{} HP:'.format(enemy.name), enemy.print_health())
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
        elif action == 'debug kill':
            enemy.hp = 0
        enemy.attack(player)
        sleep(2)
    if player.hp > 0:
        msg = 'You stand victorious! the {} is defeated.'.format(enemy.name)
        msg = formatText(msg, 'GREEN')
        print(msg)
        sleep(3)
    elif enemy.hp > 0:
        msg = 'You have been defeated!'
        msg = formatText(msg, 'RED')
        print(msg)
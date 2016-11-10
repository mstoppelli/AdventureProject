from player import player
from time import sleep
import characters
from battle import battle


def explore():
    print('You explore the area...')
    sleep(2)
    player.location.explore()


def examine(target):
    #print('running examine with target', target)
    if isinstance(target, characters.Character):
        print(target.description())
    elif target == 'me':
        print(player.description())
    elif target == 'inventory':
        player.show_inv()
    else:
        print('That\'s not a valid examination target!')

def debug(job):
    if job == 'battle':
        battle(player, characters.Rat())

def player_action():
    action = input('What would you like to do?\n')
    action = action.split()
    #print(action)
    try:
        args = action[1:]
        #print('doing', action[0], 'with args', args)
        globals()[action[0]](*args)
    except TypeError:
        print('You\'re trying to do too much!')
    except KeyError:
        print('What are you trying to do?')


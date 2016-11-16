from player import player
from time import sleep
import characters
from battle import battle

def save():
    player.save()

def load():
    player.load()

def explore():
    print('You explore the area...')
    sleep(2)
    player.location.explore()


def help():
    actions = ['explore', 'examine', 'debug', 'save', 'load']
    alist = ''
    for i in actions:
        alist = alist + str(i) + ', '
    print('Available actions: {}'.format(alist))
    input('Press enter to continue')


def examine(target):
    # print('running examine with target', target)
    if isinstance(target, characters.Character):
        print(target.description())
    elif target == 'me':
        print(player.description())
        input('Press enter to continue)')
    elif target == 'inventory':
        player.show_inv()
        input('Press enter to continue)')
    else:
        print('That\'s not a valid examination target!')


def debug(job):
    if job == 'battle':
        battle(player, characters.enemies[0])
    if job == 'reload_enemies':
        characters.load_enemies()
        print('DEBUG: enemies reloaded')
    if job == 'hurt_me':
        player.sethp(5)


def player_action():
    action = input('What would you like to do?\n')
    action = action.split()
    # print(action)
    try:
        args = action[1:]
        # print('doing', action[0], 'with args', args)
        globals()[action[0]](*args)
    except TypeError:
        print('You\'re trying to do too much!')
        sleep(2)
    except KeyError:
        print('I don\'t get what you\'re trying to do!')
        sleep(2)
    except IndexError:
        print('You do nothing.')
        sleep(2)

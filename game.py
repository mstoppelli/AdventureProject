from maps import *
from utilities import *
import battle, characters


def game_start():
    player.create_player()
    player.setLocation(StartArea())
    # print('You wake up in a dark cave...')
    # sleep(2)
    # print('You should probably get your stuff...')
    # sleep(2)
    # print('And find a way out.')
    # sleep(2)
    gameloop()

def player_action():
    action = input('What would you like to do?')
    if action == 'explore':
        player.location.explore()
    if action == 'debug battle':
        battle.battle(player, characters.Rat())

def gameloop():
    while player.is_alive():
        clear()
        print('You are in {}'.format(player.location))
        print(player.location.describe())
        player_action()

game_start()
# battle(player, Rat())

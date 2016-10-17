from player import *
from maps import *


def game_start():
    player.setLocation(Test())
    player.where_am_i()


def gen_player():  # Catch all for getting our player, in case we add args
    name = input('What is your name?')  # get their name, maybe gender too
    return Player(name)  # return a new player instance with inputted name


player = gen_player()  # THIS IS OUR PLAYER, NEVER AGAIN USE Player()
game_start()

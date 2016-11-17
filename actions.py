from player import player
from time import sleep
import characters
from battle import battle

actions = {}
def register_action(action):
    actions[action.key] = action
    #print(actions)

# def valid_action(key):
#


class Action:
    def __init__(self, key, help):
        self.key = key
        self.help = help

    def act(self, *args):
        print('You do nothing.')

    def condition(self):
        return True

    def __str__(self):
        return 'ACTION - {}'.format(self.key)

class Help(Action):
    def __init__(self):
        self.key = 'help'
        self.help = 'Type help, and then a command to see more info'
        super().__init__(self.key, self.help)

    def act(self, target=None):
        if target is None:
            msg = 'List of possible actions: '
            for i in actions.keys():
                msg = msg + str(i) + ', '
            print(msg)
            print(self.help)
            input('Press enter to continue')
        elif target in actions:
            print('{}: {}'.format(target, actions[target].help))
            input('Press enter to continue')
register_action(Help())

class Save(Action):
    def __init__(self):
        self.key = 'save'
        self.help = 'Save your character'
        super().__init__(self.key, self.help)

    def act(self):
        player.save()
register_action(Save())


class Load(Action):
    def __init__(self):
        self.key = 'load'
        self.help = 'Load your character'
        super().__init__(self.key, self.help)

    def act(self):
        player.load()
register_action(Load())

class Explore(Action):
    def __init__(self):
        self.key = 'explore'
        self.help = 'Explore the area around you'
        super().__init__(self.key, self.help)

    def act(self):
        print('You explore the area around you.')
        sleep(3)
        player.location.explore()
register_action(Explore())

class Examine(Action):
    def __init__(self):
        self.key = 'examine'
        self.help = 'Examine a target, yourself or your inventory'
        super().__init__(self.key, self.help)

    def act(self, target=None):
        if isinstance(target, characters.Character):
            print(target.description())
            input('Press enter to continue')
        elif target == 'me':
            print(player.description())
            input('Press enter to continue)')
        elif target == 'inventory':
            player.show_inv()
            input('Press enter to continue)')
        else:
            print('Examine what?')
register_action(Examine())

class Debug(Action):
    def __init__(self):
        self.key = 'debug'
        self.help = ''
        super().__init__(self.key, self.help)

    def act(self, job):
        if job == 'battle':
            battle(player, characters.enemies[0])
        elif job == 'reload_enemies':
            characters.load_enemies()
            print('DEBUG: enemies reloaded')
        elif job == 'hurt_me':
            player.sethp(5)
register_action(Debug())


def player_action():
    action = input('What would you like to do?\n')
    command = action.split()
    action = command[0]
    #print(action)
    # if action not in actions:
    #     print('I don\'t get what you\'re trying to do')
    #     sleep(2)
    #     return
    try:
        args = command[1:]
        # print('doing', action[0], 'with args', args)
        actions[action].act(*args)
    except TypeError:
        print('You\'re trying to do too much!')
        sleep(2)
    except KeyError:
        print('I don\'t get what you\'re trying to do!')
        sleep(2)
    except IndexError:
        print('You do nothing.')
        sleep(2)

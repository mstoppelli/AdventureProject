import battle, characters, items, random
from player import player
from time import sleep


class Event:
    def __init__(self, msg):
        self.msg = msg

    def run_event(self): # WHat happens when the event is run, by default just plays a message
        print(self.msg)
        sleep(3)


###TESTS###
class TestEventA(Event):
    def __init__(self):
        super().__init__('This is Event A')


class TestEventB(Event):
    def __init__(self):
        super().__init__('This is Event B')


###BATTLES###
class BattleEvent(Event):
    def __init__(self, enemy, mod=0, msg=''):
        self.enemy = enemy
        self.mod = mod
        super().__init__(msg)
        if self.msg == '':
            self.msg = 'You are fighting a {}'.format(self.enemy)
        if mod != 0:
            self.enemy.mod_enemy(self.mod)

    def run_event(self):
        battle.battle(player, self.enemy)

class RandBattle(BattleEvent):
    def __init__(self, level):
        self.enemy = characters.random_enemy(level)
        self.mod = random.randint(0, 2) #update this as we add more mods
        msg = 'You are fighting {}'.format(self.enemy)
        super().__init__(self.enemy, self.mod, msg)


###ITEMS###
class LootEvent(Event):
    def __init__(self, item):
        self.item = item
        msg = 'You find a {}!'.format(self.item.name)
        super().__init__(msg)

    def run_event(self):
        print(self.msg)
        player.add_item(self.item)
        sleep(3)


class LootGold(LootEvent):
    def __init__(self):
        super().__init__(items.Gold(5))


###EVENT TABLES### To add events, it's {Weight : Event} #FIXME do this better
EVENT_StartArea = {1:RandBattle(1)}

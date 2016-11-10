import battle, characters, items
from player import player
from time import sleep


class Event:
    def __init__(self, msg):
        self.msg = msg

    def run_event(self):
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


class RatBattle(BattleEvent):
    def __init__(self, mod=0):
        self.mod = mod
        super().__init__(characters.Rat(), self.mod)


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

###EVENT TABLES### To add events, it's {Weight : Event}
EVENT_StartArea = {}

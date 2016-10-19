import battle, characters


class Event:
    def __init__(self, msg):
        self.msg = msg

    def run_event(self):
        raise NotImplementedError

###BATTLES###
class BattleEvent(Event):
    def __init__(self, player, enemy, mod=0, msg=''):
        self.enemy = enemy
        self.player = player
        self.mod = mod
        super().__init__(msg)
        if self.msg == '':
            self.msg = 'You are fighting a {}'.format(self.enemy)
        if mod != 0:
            self.enemy.mod_enemy(self.mod)

    def run_event(self):
        battle.battle(self.player, self.enemy)

class RatBattle(BattleEvent):
    def __init__(self, player, mod=0):
        self.mod = mod
        super().__init__(player, characters.Rat(), self.mod)


###ITEMS###
class LootEvent(Event):
    def __init__(self, player, item):
        self.player = player
        self.item = item
        msg = 'You find a {}!'.format(self.item)
        super().__init__(msg)

    def run_event(self):
        print(self.msg)
        player = self.player
        player.add_item(self.item)
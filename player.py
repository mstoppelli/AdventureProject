from characters import *  # bring character functions
import items, pickle
from copy import copy


class Player(Character):  # the player
    def __init__(self, name):  # only should be run once with defaults, so no need for many inputs
        self.hp = 100  # 100 hp seems good
        self.maxhp = 100  # so we know where to heal/what not to go over
        self.inventory = []  # should hold instances of items
        self.location = None  # current location
        self.equipment = {'weapon': None, 'armor': None, 'shield': None}  # what's equipped with keywords
        self.spells = []
        super().__init__(name, 0, 2)  # set our name,

    def __str__(self):
        return "You"

    def description(self):
        msg = 'It\'s you, {}. Your HP is {}.'.format(self.name, self.hp)
        return msg

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def setLocation(self, location):
        self.location = location

    def sethp(self, hp):
        self.hp = hp

    def where_am_i(self):
        desc = 'You are in %s' % self.location
        return desc

    def get_damage(self):
        weapon = self.equipment['weapon']
        if self.equipment['weapon'] is None:
            return 1
        else:
            return weapon.dmg

    def get_equipped(self, slot):
        if slot == 'weapon' and self.equipment[slot] is None:
            return 'fists'
        elif slot == 'armor' and self.equipment[slot] is None:
            return 'naked body'
        elif slot == 'shield' and self.equipment[slot] is None:
            return 'nothing'
        else:
            return self.equipment[slot].name

    def attack(self, target):
        dmg = self.get_damage()
        target.hp -= dmg
        dmg = formatText(str(dmg), 'BOLD')
        msg = 'You attacked {} with your {}. {} took {} damage.'.format(target.name, self.get_equipped('weapon'),
                                                                        target._genpronoun(), dmg)
        print(msg)

    def print_health(self):
        hp = self.hp
        maxhp = self.maxhp
        num_bars = int(((hp / maxhp) * 10))
        bar = '[' + '*' * num_bars + ' ' * (10 - num_bars) + ']'
        bar = formatText(bar, 'GREEN')
        return (bar)

    def mod_gold(self, amt, add=True):  # modify player's gold
        if any(isinstance(gold, items.Gold) for gold in self.inventory):  # if we already have a gold value
            for gold in range(len(self.inventory)):  # loop thru inven
                #print(self.inventory[gold]) DEBUG
                if isinstance(self.inventory[gold], items.Gold):  # if we find the gold instance
                    #print('Found gold at:', self.inventory[gold]) DEBUG
                    if add is True:
                        self.inventory[gold] += items.Gold(amt)
                    else:
                        self.inventory[gold] = items.Gold(amt)
        else:
            self.inventory.append(items.Gold(amt))

    def add_item(self, item):
        self.inventory.append(item)

    def get_money(self):
        for i in self.inventory:
            if isinstance(i, items.Gold):
                return i.amt

    def show_inv(self):
        print('Your Inventory')
        print('----------')
        msg = []
        for i in self.inventory:
            msg.append(str(i))
        newmsg = '\n'.join(msg)
        print(newmsg)

    def checkitem(self, itype):
        itype = getattr(items, itype)
        for i in self.inventory:
            if isinstance(i, itype):
                #print(i, 'yes')
                return True
            else:
                #print(i, 'no')
                return False

    def create_player(self):
        name = input('What is your name?\n')
        self.name = name

    def save(self):
        with open('savefile.dat', 'wb') as save:
            pickle.dump(self, save, protocol=2)
            print('Player Saved')

    def load(self):
        with open('savefile.dat', 'rb') as save:
            ps = pickle.load(save)
            self.mod_gold(ps.get_money, add=False)
            self.inventory = copy(ps.inventory)
            self.location = ps.location
            self.spells = ps.spells
            self.name = ps.name
            self.sethp(ps.hp)
            self.maxhp = ps.maxhp
player = Player('Player')
# if __name__ == '__main__':
#     player = Player('Yas')
#     player.checkitem('Gold')
#     player.mod_gold(10)
#     player.checkitem('Gold')

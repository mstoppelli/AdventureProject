from characters import *  # bring character functions


class Player(Character):  # the player
    def __init__(self, name):  # only should be run once with defaults, so no need for many inputs
        self.hp = 100  # 100 hp seems good
        self.maxhp = 100  # so we know where to heal/what not to go over
        self.inventory = []  # should hold instances of items
        self.location = None  # current location
        self.equipment = {'weapon': None, 'armor': None, 'shield': None}  # what's equipped with keywords
        super().__init__(name, 0, 2)  # set our name,

    def __str__(self):
        return "You"

    def description(self):
        inv = []
        for i in self.inventory:
            inv += i.description
            inv += '\n'
        for i in inv:
            print(i)

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def setLocation(self, location):
        self.location = location

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
        msg = 'You attacked {} with your {}. {} took {} damage.'.format(target.name, self.get_equipped('weapon'), target._genpronoun(), dmg)
        msg = formatText(msg, 'RED')
        print(msg)

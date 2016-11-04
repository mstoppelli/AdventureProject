from utilities import *
#----------Base Character Classes-------------
class Character:  # Generic character class
    def __init__(self, name, disposition,
                 gender):  # Initialize, we want to input a name, disposition and gender for every character
        self.name = name  # Name, string
        self.disposition = disposition  # Disposition, value from -100 to 100
        self.gender = gender  # 0 for males, 1 for females, 2 for other

    def _genpronoun(self):  # Decide on a pronoun
        pronouns = ['He', 'She', 'It']  # Male, Female, Other
        return pronouns[self.gender]  # 0:Male, 1:Female, 2:Other

    def __str__(self):  # What this object is printed as
        return self.name  # print(Character()) Should just return it's name

    def calcdisp(self):  # Nice disposition name
        dispositions = ['Hostile', 'Neutral', 'Friendly']  # <100, <51, <100
        if self.disposition < 0:
            return formatText(dispositions[0], 'RED')
        elif self.disposition <= 50:
            return dispositions[1]
        else:
            return formatText(dispositions[2], 'GREEN')

    def description(self):  # Should be used when we describe a character
        line1 = 'You see {}. {} is {}.\n'.format(self.name, self._genpronoun(),
                                                 self.calcdisp())  # Their name, gender and disposition
        return line1


class Enemy(Character): # for combat specific vars, maybe make allies later
    def __init__(self, name, gender, hp, dmg): # we take same vars
        self.hp = hp # assign new ones (health and dmg)
        self.dmg = dmg
        self.maxhp = self.hp
        super().__init__(name, -100, gender) # pass the first 2 vars on, but disposition is always -100. they're enemies

    def _vowelcheck(self): # if hte name starts with a vowel, use an before name. else, a
        if self.name[0] in ['A', 'E', 'I', 'O', 'U']:
            return 'an'
        else:
            return 'a'

    def __str__(self): # enemies referred to in generic name, not on name basis
        return '{} {}'.format(self._vowelcheck(), self.name)

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def attack(self, target):
        target.hp -= self.dmg
        dmg = self.dmg
        msg = '{} attacks {}. You took {} damage.'.format(self.name, target.name, dmg)
        msg = formatText(msg, 'RED')
        print(msg)

    def print_health(self):
        hp = self.hp
        maxhp = self.maxhp
        num_bars = int(((hp / maxhp) * 10))
        bar = '[' + '*' * num_bars + ' ' * (10 - num_bars) + ']'
        bar = formatText(bar, 'RED')
        return(bar)

    def mod_enemy(self, mod):
        mods = [None, ['Strong', 2], ['Weak', -1]]
        if mod != 0:
            self.name = self.name + ' ' + mods[self.mod][0]
            self.dmg += mods[self.mod][1]

#---------Enemy Definitions-------
class Rat(Enemy):
    def __init__(self):
        self.name = 'Rat'
        self.gender = 2
        self.hp = 10
        self.dmg = 2
        super().__init__(self.name, self.gender, self.hp, self.dmg)

# jim = Character('Jim', 50, 0)
# jane = Character('Jane', 51, 1)
# in_room = [Rat(), jim, jane]
# for i in in_room:
#     print(i)
#     print(i.description())

from utilities import *
import player


# schools : 0:arcane, 1:fire, 2:earth, 3:water, 4:holy, 5:dark
def is_player(object):
    if isinstance(object, player.Player):
        return True
    else:
        return False


class Spell:
    def __init__(self, name, cost, school, eff_text):
        self.name = name
        self.cost = cost
        self.school = school
        self.eff_text = eff_text

    def _format_school(self):
        colors = {2: 'GREEN', 4: 'YELLOW', 1: 'RED', 3: 'BLUE', 5: 'BOLD', 0: 'CYAN'} #
        return colors[self.school]

    def school_name(self):
        schools = {0: 'Arcane', 1: 'Fire', 2: 'Earth', 3: 'Water', 4: 'Holy', 5: 'Dark'}
        return schools[self.school]

    def __str__(self):
        name = formatText(self.name, self._format_school())
        msg = '{} (Cost: {}) | {}'.format(name, self.cost, self.school_name())
        return msg

    def cast_effect(self, caster):  # Everything that should happen upon the spell being casted should go here
        raise NotImplementedError


class CombatSpell(Spell):
    def __init__(self, name, cost, school, eff_text, dmg):
        self.dmg = dmg
        super().__init__(name, cost, school, eff_text)

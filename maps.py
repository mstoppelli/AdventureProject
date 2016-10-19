from utilities import *
from player import player
from mevents import *


# --------Base Types--------
class Map:
    def __init__(self, name, description, adj_locations, events):
        self.name = name
        self.description = description
        self.adj_locations = adj_locations
        self.actions = []
        self.events = events

    def __str__(self):
        return formatText(self.name, 'BOLD')

    def describe(self):
        return self.description

    def explore(self):
        raise NotImplementedError



class Test(Map):
    def __init__(self):
        super().__init__(name='TESTING AREA', description='Fee fi fo fun', adj_locations=[])


class StartArea(Map):
    def __init__(self):
        super().__init__(name='Dark Cave',
                         description='A dark cave you\'ve awoken in. The walls are damp, and the air is thick.'
                                     'You should probably leave soon.',
                         adj_locations=[],
                         events = [RatBattle(player)])

    def explore(self):
        raise NotImplementedError
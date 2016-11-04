from utilities import *
from mevents import *
import random


# --------Base Types--------
class Map:
    def __init__(self, name, description, adj_locations, events):
        self.name = name
        self.description = description
        self.adj_locations = adj_locations
        self.events = events

    def __str__(self):
        return formatText(self.name, 'BOLD')

    def describe(self):
        return self.description

    def build_events(self):
        weighed_events = []  # empty list we'll append
        for key in self.events:  # loop through each event key
            for i in range(key + 1):  # take the range of 0 to the key inclusive
                weighed_events.append(self.events[key])  # for each number in the range, add the event to our list
        return weighed_events

    def explore(self):
        weighed_events = self.build_events()
        re = random.randint(0, len(weighed_events) - 1)
        chosen_event = weighed_events[re]
        chosen_event.run_event()


class Test(Map):
    def __init__(self):
        super().__init__(name='TESTING AREA', description='Fee fi fo fun', adj_locations=[], events={})


class StartArea(Map):
    def __init__(self):
        super().__init__(name='Dark Cave',
                         description='A dark cave you\'ve awoken in. The walls are damp and the air thick.'
                                     ' You should probably leave soon.',
                         adj_locations=[],
                         events={25: RatBattle(), 75: TestEventB()})

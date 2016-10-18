from utilities import *
import items

# --------Base Types--------
class Map:
    def __init__(self, name, description, adj_locations):
        self.name = name
        self.description = description
        self.adj_locations = adj_locations

    def __str__(self):
        return formatText(self.name, 'BOLD')

    def describe(self):
        return self.description


class Test(Map):
    def __init__(self):
        super().__init__(name='TESTING AREA', description='Fee fi fo fun', adj_locations=[])

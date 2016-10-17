class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return '%s | %s | Value : %d' % (self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name='Gold', description='Very shiny',value=self.amt)
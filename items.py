class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return '%s | %s | Value: %d' % (self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name='Gold', description='Valuable currency',value=self.amt)

    def __add__(self,other):
        return Gold(self.amt+other.amt)

class Equipment(Item):
    def __init__(self, name, description, value, slot):
        self.slot = slot
        super().__init__(name, description, value)

    def __str__(self):
        slots = ['Armor', 'Shield', 'Weapon']
        return '{} | {} | Slot: {} | Value: {}'.format(self.name, self.description, slots[self.slot], self.value)



# if __name__ == '__main__':
#     gold1 = Gold(10)
#     print(gold1)
#     gold1 += Gold(5)
#     print(gold1)
# print(Equipment('Shield', 'Very sturdy', 5, 1))
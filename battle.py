def take_action():
    action = input('What would you like to do?')
    actions = ['attack', 'defend', 'flee', 'item']
    if action in actions:
        return action
    else:
        print('Please input a valid action.')
        return take_action()

def fight(player, enemy):
    print('You are fighting a %s!' % enemy)
    while enemy.is_alive() and player.is_alive():
        action = take_action()

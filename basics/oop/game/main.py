'''We are executing on main using imported classes'''
from enemy import *

enemy = Enemy_alien()

'''we can add another feature and make it part of the class'''
enemy.type_of_enemy= 'Lizard'

print(f'My name is {Enemy_alien.name}, I have {Enemy_alien.eyes} eyes and' + 
    f"I'm a {Enemy_alien.attack_speed} {enemy.type_of_enemy}!")


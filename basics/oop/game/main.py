'''We are executing on main using imported classes'''
from Enemy import *
from Warrior import *
from Amazon import *

# lizard = Enemy_alien(the_name= 'Rarg', health_points = 10, eyes = 3, attack_speed = 'slow', 
#                     attack_damage = 2, type_of_enemy='monkey')

'''we can add another feature and make it part of the class'''
# # enemy.type_of_enemy= 'Lizard'
# # enemy_type = lizard.get_type_of_enemy()
# warrior = Warrior(10, 'medium', 2)
# warrior.enemy_talk()
# warrior.walk_forward()
# warrior.attack()

# print(f"I'm a {warrior.attack_speed} {warrior.get_type_of_enemy()}!")

# print(warrior)

'''This is the Battle'''
def battle(e: Enemy):
    e.enemy_talk()
    e.attack()
    
warrior = Warrior(10, 'medium', 2)
amazon = Amazon(7, 'fast', 1)
    
battle(amazon)
battle(warrior)

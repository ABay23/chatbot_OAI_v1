'''We are executing on main using imported classes'''
from enemy import *

lizard = Enemy_alien(the_name= 'Rarg', health_points = 10, eyes = 3, attack_speed = 'slow', 
                    attack_damage = 2, type_of_enemy='monkey')

'''we can add another feature and make it part of the class'''
# enemy.type_of_enemy= 'Lizard'
enemy_type = lizard.get_type_of_enemy()
lizard.enemy_talk()
lizard.walk_forward()
lizard.attack()



print(f'My name is {lizard.the_name}, I have {lizard.eyes} eyes and' + 
    f"I'm a {lizard.attack_speed} {enemy_type}!")

print(lizard)


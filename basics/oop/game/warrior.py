'''Warrior class from enemy class'''
from enemy import *

class Warrior(Enemy):
    def __init__(self, health_points, attack_speed ,attack_damage):
        super().__init__(type_of_enemy = 'Warrior', health_points = health_points,
                        attack_damage = attack_damage, attack_speed = attack_speed)
        
    def enemy_talk(self):
        print(f'Warrions are the best!')
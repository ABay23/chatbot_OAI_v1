'''Warrior class from enemy class'''
from Enemy import *

class Warrior(Enemy):
    def __init__(self, health_points, attack_speed ,attack_damage):
        super().__init__(type_of_enemy = 'Warrior', health_points = health_points,
                        attack_damage = attack_damage, attack_speed = attack_speed)
        
    def enemy_talk(self):
        print(f'Warrions are the best!')
        
    def attack(self):
            print(f'Enemy {self.get_type_of_enemy()} attack with the power of an axe and {self.attack_damage} damage!')

'''Amazon class from enemy class'''
from Enemy import *

class Amazon(Enemy):
    def __init__(self, health_points, attack_speed ,attack_damage):
        super().__init__(type_of_enemy = 'Amazon', health_points = health_points,
                        attack_damage = attack_damage, attack_speed = attack_speed)
        
    def enemy_talk(self):
        print(f'Amazons Roaaaar!')
        
    def attack(self):
            print(f'Enemy {self.get_type_of_enemy()} attack with the power of a spear doing {self.attack_damage} damage 2 times!')
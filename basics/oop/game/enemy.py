'''This is the Enemy Class with the Enemy State and methods'''

class Enemy:
    def __init__(self, health_points: int = 10, 
                attack_speed : str ='medium',attack_damage : int = 1,
                type_of_enemy :str = 'Lizard'
                ):
        self.health_points = health_points
        self.attack_speed = attack_speed
        self.attack_damage = attack_damage
        self.__type_of_enemy = type_of_enemy
        
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    # def set_type_of_enemy(self, type_of_enemy):
    #     self.__type_of_enemy = type_of_enemy
    
    def enemy_talk(self):
        print('Woof Woof')
        
    def attack(self):
        print(f'Enemy {self.__type_of_enemy} attack with {self.attack_damage}')
        
    def walk_forward(self):
        print(f'Enemy {self.__type_of_enemy} walks closer to you')
        
    
    
import random
from models import *

new_hp = 55
new_a_atk = 10
a_atk = 10
new_b_atk = 10
b_atk = 20
hero_1 = Hero('Лолыч', 55, random.randint(a_atk,b_atk))
hero_2 = Hero('Сигмер', 80, 20)

new_monster_hp = 45
monster_1 = Monster('Жопыч', 45, random.randint(12,19))
monster_2 = Monster('Крысонька', 20, 20)

import random
from personages import *




heroes = {
    "Л" : Hero('Лолыч', 50, 15, "Маг")
}

for hero_key, hero_value in heroes.items():
    print(f'''\033[0;41m\033[0;31mИмя - {hero_value.name}\033[0m
• Здоровье - {hero_value.hp}
• Атака - {hero_value.strength}
• Тип - {hero_value.Htype}\n
''')
    
print('''\033[0;43mВыберите Персонажа:\033[0m
• Л - Лолыч
''')



while monster_1.hp > 0 or hero_1.hp > 0:
    input(hero_1.name + ', Нажми ENTER Для Атаки\n')
    print('Атака')
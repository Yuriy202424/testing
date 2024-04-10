import random
from personages import *
from models import *




heroes = {
    "Л" : Hero('Лолыч', 50, 15)
}

for hero_key, hero_value in heroes.items():
    print(f'''\033[0;41m\033[0;31mИмя - {hero_value.name}\033[0m
• Здоровье - {hero_value.hp}
• Атака - {hero_value.strength}
''')
    
print('''\033[0;43mВыберите Персонажа:\033[0m
• Л - Лолыч
''')


while True:
    while monster_1.hp > 0 or hero_1.hp > 0:
        input(hero_1.name + ', Нажми ENTER Для Атаки\n')
        hero_1.strength = random.randint(a_atk,b_atk)
        monster_1.hp = monster_1.hp - hero_1.strength
        if monster_1.hp > 0:
            print(f'Атака, вы нанесли {hero_1.strength} урона и у монстра осталось {monster_1.hp} хп!')
        elif monster_1.hp <= 0:
            print('Персонаж прорубает топором череп монстра!')
            
        

        monster_1.strength = random.randint(12,19)
        if monster_1.hp > 0:
            if hero_1.hp > 0:
                hero_1.hp = hero_1.hp - monster_1.strength
                print(f'Атака врага, он нанёс вам {monster_1.strength} урона и у вас осталось {hero_1.hp} хп! \n')

            elif hero_1.hp <= 0:
                hero_1.hp = hero_1.hp - monster_1.strength
                print('Монстр рвёт персонажа в клочья!')
                break

        elif monster_1.hp <= 0:
            print(f'Монстр умирает пытаясь ударить вас!')

        

        if monster_1.hp <= 0 and hero_1.hp > 0:
            print('Ура пабеда')
            print('Вы становитесь сильнее после драки! (+10 к хп и +5 к силе)')
            new_hp += 10
            hero_1.hp = new_hp

            a_atk += 5
            b_atk += 5
            print(f'Персонаж стал более сильным! Его здоровье - {hero_1.hp}\n')
            new_monster_hp += 18
            monster_1.hp = new_monster_hp
            break
        
        elif monster_1.hp > 0 and hero_1.hp < 0:
            print('Проигрыш')
            break
        
        elif monster_1.hp <= 0 and hero_1.hp <= 0:
            print('Оба умерли')
            break
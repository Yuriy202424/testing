import random
from personages import *
from models import *



heroes = {
    'Л': Hero('Лолыч', 55, random.randint(a_atk,b_atk)),
    'С': Hero('Сигмер', 80, 20)

}

for hero_key, hero_value in heroes.items():
    print(f'''\033[0;41m\033[0;31mИмя - {hero_value.name}\033[0m,
• Здоровье - {hero_value.hp},
• Cила - {hero_value.strength}\n''')

print('''\033[0;43mВыберите Персонажа:\033[0m
• С - Сигмер
• Л - Лолыч
''')


selected_hero = None

while selected_hero is None:
    u_input = input("Выберите Персонажа: ").upper()
    if u_input in heroes:
        selected_hero = heroes[u_input]
        print(f"\033[0;43mВыбран персонаж: {selected_hero.name}\033[0m\n\033[0;43m\033[0m")
    else:
        print("Некорректный выбор персонажа. Попробуйте еще раз.")


crit_chance = random.randint(1,10)


while True:
    while monster_1.hp > 0 or selected_hero.hp > 0:
        input(selected_hero.name + ', Нажми ENTER Для Атаки\n')
        selected_hero.strength = random.randint(a_atk,b_atk)
        if crit_chance >= 8:
            selected_hero.strength += 20
        
        else:
            pass
        
        monster_1.hp = monster_1.hp - selected_hero.strength
        if monster_1.hp > 0:
            print(f'Атака, вы нанесли {selected_hero.strength} урона и у монстра осталось {monster_1.hp} хп!')
        elif monster_1.hp <= 0:
            print('Персонаж прорубает топором череп монстра!')
            
        

        monster_1.strength = random.randint(12,19)
        if monster_1.hp > 0:
            if selected_hero.hp > 0:
                selected_hero.hp = selected_hero.hp - monster_1.strength
                print(f'Атака врага, он нанёс вам {monster_1.strength} урона и у вас осталось {selected_hero.hp} хп! \n')

            elif selected_hero.hp <= 0:
                selected_hero.hp = selected_hero.hp - monster_1.strength
                print('Монстр рвёт персонажа в клочья!')
                break

        elif monster_1.hp <= 0:
            print(f'Монстр умирает пытаясь ударить вас!')

        

        if monster_1.hp <= 0 and selected_hero.hp > 0:
            print('Ура пабеда')
            print('Вы становитесь сильнее после драки! (+10 к хп и +5 к силе)')
            new_hp += 10
            selected_hero.hp = new_hp

            a_atk += 5
            b_atk += 5
            print(f'Персонаж стал более сильным! Его здоровье - {hero_1.hp}\n')
            new_monster_hp += 18
            monster_1.hp = new_monster_hp
            break
        
        elif monster_1.hp > 0 and hero_1.hp < 0:
            print('Проигрыш')
            break
        
        elif monster_1.hp <= 0 and selected_hero.hp <= 0:
            print('Оба умерли')
            break
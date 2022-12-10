# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
import random
candyes=117
print('Начало игры')
input("Press Enter to continue...")
print('Введите имя первого игрока:')
name1=input()
print(f'Привет, {name1}')
print('Введите имя второго игрока:')
name2=input()
print(f'Привет, {name2}')
print(f'Правила игры: На столе {candyes} конфет. Игроки ходят друг за другом')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
input("Нажмите Enter чтобы определить кто делает первый ход")
players=[name1, name2]
move=random.choice(players)
print(f'Первым ходит: {move}')
input("Нажмите Enter для начала хода")
while candyes>0:
    gameover=False
    if move==name1:
        needtomove=1
        while needtomove>0:
            print(f'{name1} введите кол-во конфет:')
            move=int(input())
            if move>0 and move<29:
                needtomove=0
                candyes-=move
                move=name2
                print(f'Осталось {candyes} конфет')
                if candyes<29:
                    print(f'Наш победитель  {move}')
                    gameover=True
                    break
            else:
                print('Берите не больше 28 конфет')
                needtomove=1
        if gameover:
            break    
    elif move==name2:
        needtomove=1
        while needtomove>0:
            print(f'{name2} введите кол-во конфет:')
            move=int(input())
            if move>0 and move<29:
                needtomove=0
                candyes-=move
                move=name1
                print(f'Осталось {candyes} конфет')
                if candyes<29:
                    print(f'Наш победитель  {move}')
                    gameover=True
                    break
            else:
                print('Берите не больше 28 конфет')
                needtomove=1
        if gameover:
            break



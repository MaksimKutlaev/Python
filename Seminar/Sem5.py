# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

# from math import pi

# def format_by_mask(num: float, accuracy: float) -> float:
#     """"форматирует число по заданной маске"""
#     accuracy=str(accuracy)
#     accuracy=len(accuracy[accuracy.find('.')+1::])
#     print(accuracy)
#     return float(f'{pi:0.{accuracy}f}') #

# d=input('Введите точность в формате "0.001":')
# print(format_by_mask(pi, d))

# 3'. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# from random import randint as rnd

# mass=[rnd(1,4) for i in range(12)]
# print(f'Исходный список {mass}')
# print(f'Список уникальных элементов: {list(set(mass))}') #set возвращает уникальные значения + list для упорядочевния и обработки

# mass = [i for i in mass if mass.count(i)==1] #лист комплехешен
# print(f'Uniq: {mass}')

# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. 
# from functions import create_pol_file
# from functions import create_polinom

# k=int(input())

# print(f'Сгенерированный полином {create_polinom(k)}')
# create_pol_file(create_polinom(k))

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# # В file1.txt :

from functions import create_pol_file
from functions import create_polinom
from sympy import simplify

degree=int(input('Задайте степень: '))

pol1=create_polinom(degree) #генерируем полиномы
pol2=create_polinom(degree)

filname1='first'   #Имена создаваемых файлов
filname2='second'
sum_filename='sum'

create_pol_file(pol1, filname1)
create_pol_file(pol2, filname2)

with open(f'Seminar/{filname1}.txt','r') as f1: #считываем с файла информацию
    f_pol=f1.read()
    print(f'Первый полином: {f_pol}')

with open(f'Seminar/{filname2}.txt','r') as f2:
    s_pol=f2.read()
    print(f'Второй полином:{s_pol}')

sum_of_pols=simplify(f_pol +'+'+s_pol) #складываем полиномы
sum_of_pols=str(sum_of_pols)

print(f'Сумма: {sum_of_pols}')

with open(f'Seminar/{sum_filename}.txt','w') as s: #записываем в файл
    s.write(sum_of_pols)







# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num=float(input('Введите число'))
print(num)
sum=0
while num>0:
    sum=sum+(num%10)
    num=num//10
    for i in str(num):
        if i !='.':
            sum +=int(i)
print(int(sum))

# x = input('Введите число ')

# def summa(x):                            #Функция нахождения суммы чисел в заданном числе
#     if float(x) < 0:                            #Проверка на знак перед числом
#         x = float(x) * (-1)
#     number = 0

#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number

   
# print(f'Сумма чисел равна {summa(x)}')



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
N=int(input('Введите число '))
s=[]
product=1
while N>0:
    for i in range(N):
        product*=i+1
        N=N-1
        # print(product,end=' ')
        s.append(product)
print(s)
    

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

n=int(input('Введите число '))
res=0
s=[]
while n>0:
    for i in range(n):
        res=(1+1/n)**n
        n=n-1
        # print(res,end=' ')
        s.append(res)
s.reverse()
print(s)



# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

N=int(input('Введите число'))
s=[]
for i in range(-N,N):
    s.append(i)
print(s)
a=int(input())
b=int(input())
pr=0
for i in s:
    pr=s[a]*s[b]
print(f'{a,b} -> {pr}')



# Реализуйте алгоритм перемешивания списка.

from random import shuffle
list=[1,2,3,4,5]
shuffle(list)
print(list)
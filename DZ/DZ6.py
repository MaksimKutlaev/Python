# 3'. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

a=[2, 3, 2, 45, 13, 3, 1]
spisok=[]
spisok=[set (i for i in a if i not in spisok)]
print(list(*spisok))


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(my_list)
print(sum(my_list[1::2]))

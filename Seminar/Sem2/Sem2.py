# 1'. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# print('Введите число ')
# n = int(input())
# a = 1
# b = -3
# result=0
# for i in range(n):
#     result = a * b ** i
#     print(result,end=' ')



# 2'. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# print('Введите число ')
# n = int(input())
# a = 4
# d = {i+1: a + 3*i for i in range(n)}
# print (d)

# 3'. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# Пример :
# абвгдабвгд -> 2
# абв

print('Введите строку')
a = str(input())
print('Введите строку')
b = str(input())

print (a.count(b))
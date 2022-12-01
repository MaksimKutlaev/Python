#Вывести квадрат числа

# a=int(input())
# print(f'Квадрат числа {a**2}')

# Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

# a=int(input())
# b=int(input())

# if a==b**2:
#     print(f' Число {a} квадрат  {b}')
# else:
#     print (f' Число {a} не квадрат {b}')

# if a==b**2:
#     print('Ok')
# elif b==a**2:
#     print('Ok')
# else:
#     print('No')

#Найти максимальнок число

# max=int(input())
# for i in range(4):
#     b=int(input())
#     if b>max:
#         max=b
# print(max)

# a=input().split()
# print(max(a))

# a = list(map(int, input().split()))
# print(max(a))

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:* 
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# print('Введите число ')
# N=int(input())
# for i in range (-N,N+1):
#     print(i, end=' ')

# n = int(input())
# a = []
# for i in range(-n, n+1):
#     a.append(i)
# print(*a)

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# print('Введите вещественное число:')
# a = float(input())

# print(int(a * 10) % 10)


# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно ((5 и 10) или 15), но не 30.
#45 ok
#20 ok
#150 no

# print('Введите число: ')
# a = int(input())

# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print('Yes')
# else:
#     print('No')
 


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
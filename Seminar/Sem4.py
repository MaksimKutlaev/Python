#Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# print("Введите числа через порбел: ")
# mass = list(map(int, input().split()))
# print(f"Минимальное введенное число: {min(mass)}\nМаксимльное введенное число: {max(mass)}")

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения (D = b^2-4ac, x1 = (-b+/- sqtr(D))/a)

# 2) с помощью дополнительных библиотек Python(sympy, scipy)(Дополнительно)


# a = float (input("введите значения уравнения a: "))
# b = float (input("введите значения уравнения b: "))
# c = float (input("введите значения уравнения c: "))
# d = (b**2)-(4*a*c)
# if d < 0:
#     print("Корней нет")
# elif d == 0:
#     print(f"Корень уравнения = {-b / (2 * a)}")
# else:
#     print(f"Корень уравнения x1 = {round((- b + d**0.5) / (2 * a), 3)}")
#     print(f"Корень уравнения x2 = {round((- b - d**0.5) / (2 * a), 3)}")
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример:
# 4, 5 -> 20
# 4,6 -> 12
# math.gcd(30, 18)


# Пример:
# Найти НОД для 30 и 18.
# 30 / 18 = 1 (остаток 12)
# 18 / 12 = 1 (остаток 6)
# 12 / 6 = 2 (остаток 0)
# Конец: НОД – это делитель 6.
# НОД (30, 18) = 6
# a = int (input("Введите число a: "))
# b = int (input("Введите число b: "))
# mass = [a, b]
# temp_ostatok = max(mass) % min(mass)
# temp_min = min(mass)
# while temp_ostatok != 0:
#     temp_ostatok_while = temp_min % temp_ostatok
#     temp_min = temp_ostatok
#     temp_ostatok = temp_ostatok_while
# print(f"НОД: {temp_min}")
# print(f"НОК: {a * b // temp_min}")

import sympy
from sympy.solvers import solve
from sympy import Symbol
a = float (input("введите значения уравнения a: "))
b = float (input("введите значения уравнения b: "))
c = float (input("введите значения уравнения c: "))

def fun(a,b,c):
    x = Symbol('x')
    return solve(f'{a}*x**2+{b}*x+{c}', x)
print('Корни уравнения:', *fun(a, b, c))
# expr = a*x**2 + 3*x +  2 
# expr1 = sympy.sympify(expr)
# expr1.subs(x, 2)

# import sympy


# x = sympy.Symbol('x')

# a = input('Input eq:')
# print(sympy.solve(a, x))
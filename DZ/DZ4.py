# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  
# x=4-4/3+4/5-4/7+4/9-...
import math
print('Введите точность округления числа Пи ')
d=(input())
d=(len(str(d).split('.')[1]))
print(d)
print(round(math.pi, d))


# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

print('Введите натуральное число n:')
n=int(input())
res=[]
i=2
while i*i<=n:
    while n%i==0:
        n//=i
        res.append(i)
    i+=1
if n>1:
    res.append(n)
res1=[]
for i in res:
    if i not in res1:
        res1.append(i)
print(res)
print(res1)





# 3'. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

a=[2, 3, 2, 45, 13, 3, 1]
spisok=[]
for i in a:
    if i not in spisok:
        spisok.append(i)
    
print(spisok)



# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 


from random import randint
 
print('Введите натуральную степень k:')
k = int(input())
 
def write_file(st):
    with open('DZ/Task04.txt', 'w') as data:
        data.write(st)
 
def coef_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 101))    
    return list
    
def polinomial(sp):
    list = sp[::-1]
    pol = ''
    if len(list) < 1:
        pol = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                pol += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    pol += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                pol += f'{list[i]}x'
                if list[i + 1] != 0:
                    pol += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                pol += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                pol += ' = 0'
    return pol
 
coef = coef_list(k)
write_file(polinomial(coef))

# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
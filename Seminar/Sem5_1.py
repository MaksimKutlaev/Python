# 1. Задано N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i]-1=A[i-1].
# Найдите число.
# * 1 2 3 4 6 7->5
# * 1 3 ->2

# from random import randint as rnd

# numbers=[rnd(1,9) for i in range(10)]

# print(set(numbers))


s = '1 2 4 6 7'
a = [int(x) for x in s.split()]
print(a)

for i in range(len(a)):
    if i==0:
        continue
    elif a[i]-a[i-1]>1:
        print(a[i]-1)


# 2. Дан список чисел. Создайтее список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1,5,2,3,4,6,1,7]=>[1,2,3] или [1,7] или [1,6,7] и т.д.

spisok=[1, 5, 2, 3, 4, 6, 1, 7]
spisok2=[]
min=spisok[0]
spisok2.append(min)
for i in range(len(spisok)):
    if spisok[i]>min:
        min=spisok[i]
        spisok2.append(spisok[i])
    
print(spisok2)

# # 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# # *'абвгд гдежз жзе абв ыопыпт'-> 'гдежз жзе ыопыпт'

# stroka='абвгд гдежз жзе абв ыопыпт'
# mass=stroka.split()
# print(mass)
# res='абв'
# # find=stroka.find('абв')
# for i in mass:
#     if (i.find(res))!=-1:
#         mass.remove(i)
# print(mass)

del_st=lambda x,y:" ".join([i for i in x.split() if y not in i])

print(del_st('абвгд гдежз жзе абв ыопыпт', 'абв'))
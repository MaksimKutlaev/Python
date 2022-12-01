# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

spisok= [2,3,5,9,3,5,7,9,1]
summ=0
# notchet=[]
for index in range(len(spisok)):
    if not index%2==0:
        # notchet.append(index)
        summ+=spisok[index]
print(summ)
# print(sum(notchet))


# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

spisok=[2, 3, 4, 5, 6, 7, 8]
product_list=[]
product=0
index_last=spisok[-1]
for index in range(int(len(spisok)/2+1)):
    # print(index_last)
    product=spisok[index]*index_last
    # print(spisok[index])
    index=index+1
    index_last=index_last-1
    product_list.append(product)
    
print(product_list)


# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# # между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
spisok=[1.1, 1.2, 3.1, 5, 10.01]
drobi=[]
n=0
for i in spisok:
    if i%1!=0:
        n=round(i%1, 3)
        drobi.append(n)
max_num=max(drobi)
min_num=min(drobi)
print(max_num)
print(min_num)
result=min_num-min_num
print(result)
# print(drobi)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('Введите число:')
n=int(input())
print(bin(n).replace("0b",""))


#  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# F−n = (−1)n+1Fn
# Fn = F(n+2)−F(n+1)

print('Введите число:')
k=int(input())
f1=f2=1
negifib=[]
for i in range(2, k):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')

    negifib.append(f2)
print(negifib)
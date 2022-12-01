# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['ssss', 'sngujn556', 56] -> Yes
# ['56', 'sgnbsb'] -> No

# spisok = ['123', 1.1 , 'sos', '!!!', '__']

# n = 0
# for i in spisok:

#     if type(i) == int or type(i) == float:
#         n += 1
# if n > 0:
#     print('Yes') 
# else:
#     print('No')


# mass = ['ssss', 'sngujn556', '44']
# types = [str(type(i)) for i in mass]
# if "<class 'int'>" in types or "<class 'float'>" in types:
#     print('Yes')
# else:
#     print('No')

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

stroka = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
t = 0
p = 0
pos =0

n = input('введите значение ')
while p < 2 and t <len(stroka) - 1:
    
    if stroka[t] == n:
        p += 1
        pos =t
    t += 1 
if p >1:
    print(pos)
else:
    print(-1)


mass = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
a= 'qwe'

try:
    mass.remove(a)
    print((mass.index(a))+1)
except ValueError:
    print(-1)

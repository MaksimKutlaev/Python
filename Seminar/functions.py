import sympy
from random import randint as rnd

def create_polinom(k: int, simple: bool=True)->str:
    """"Генерирует полином со случайным коэффициентами степени К
    simple = False верент полином без сокращения нулевых коэффициентов"""
    polinom=''
    for i in range(k,-1,-1):   #начинаем с конца
        polinom+=f'{rnd(0,2)}*x**{i}+'
        if i ==0:
            polinom +=f'{rnd(0,100)}*x**{i}' 
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

def create_pol_file(polinom: str, filename: str='new'):
    """"Записывает полином в файл, дополнительно можно указать имя файла"""
    with open(f'Seminar/{filename}.txt','w') as f:
        f.write(polinom)
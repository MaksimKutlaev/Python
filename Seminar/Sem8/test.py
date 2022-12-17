def edit_str(base, result):
    base[base.index(result)][base[base.index(result)].index(input('Введите элемент который хотите заменить'))] = input(f'Введите новое значение: ') #base.index вщзвращает результат
    return base

def find_contacts(base, stroka):
    for i in base:
        if stroka in i:
            return i

# base = [['1','2','3'],['4','5','6']]

# print(edit_str(base, find_contacts(base, '1')))
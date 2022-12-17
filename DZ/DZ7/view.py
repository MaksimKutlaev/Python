def choose_mode():
    print(f"Выберите супер Режим:\nПоиск контакта - 1\nДобавить новый контакт - 2")
    return int(input(f"Введите 1 или 2: "))

def serch_contact():
    return input(f'Выполните поиск контакта: ')
    

def new_contact():
    print('Введите имя: ')
    name=input()
    print('ВВедите номер: ')
    phone=input()
    return f'{name}; {phone}'

def show_contact(result):
    for i in result:
        print(f'Результат: {i}')

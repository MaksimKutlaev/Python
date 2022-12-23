def choose_mode():
    print(f"Выберите Режим:\nПоиск контакта - 1\nДобавить новый контакт - 2\nИзменить контакт - 3\nУдалить контакт - 4")
    return int(input(f"Введите 1 - 2 - 3 - 4: "))

def serch_contact():
    return input(f'Выполните поиск контакта: ')
    
def new_contact():
    print('Введите имя: ')
    name=input()
    print('Введите профессию: ')
    prof=input()
    print('ВВедите номер: ')
    phone=input()
    print('ВВедите e-mail: ')
    email=input()
    return f'{name}; {prof}; {phone}; {email}'




def show_contact(result):
    for i in result:
        print(f'Результат: {i}')
        
def resume_app():
    print(f"Продолжить?:\nДа - 1\nНет - 2")
    return int(input(f"Введите 1 или 2: "))
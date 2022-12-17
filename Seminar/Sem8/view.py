def read_stroka():
    my_lines = []
    with open('Coding\Sem151222\LecFile.csv', 'r') as f:
            for i in f:
                my_lines.append(i.split(';'))
    print(my_lines)

def poisk_info():
    return input('Введите информацию для поиска')

def choice_mode():
    return input('Введите режим работы: 1 - добавление, 2 - поиск, 3 - редактирование, 4 - удаление')


def new_contact():
    name_users = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    job_title = input('Введите должность: ')
    emale_name = input('Введите электронный почтовый адрес: ')
    return f'{name_users} || {second_name} || {job_title} || {emale_name}'


def show_found(result):
    print('результаты поиска: ')
    for i in result:
        print(i)
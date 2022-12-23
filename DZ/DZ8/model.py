def search_contact(base,contact):
    contacts=base.split('\n')
    flag=True
    result=[]
    for i in contacts:
        if contact in i:
            flag=False
            result.append(i)
    if flag:
        result.append('Контакт не найден')
    return result


def del_contact():
    pass

def edit_contact():
    pass

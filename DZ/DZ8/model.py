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

# def new_id(base):
#     if len(base.split('\n'))==0:
#         return 1
#     else:
#         return int(base.split('\n')[len(base.split('\n')-1)].split(';')[0])+1


def del_contact(base,result):
    base=base.split('\n')
    base.remove(result)
    return base

def edit_contact(base,contact,new_contact):
    base=base.split('\n')
    id=contact.split(';')[0]
    base[base.index(contact)]=id+';'+new_contact
    return base 

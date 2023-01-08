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

def search_contact_by_id(base,id_str):
    contacts=base.split('\n')
    flag=True
    result=[]
    for i in contacts:
        contact_data=i.split('; ')
        if id_str==contact_data[0]:
            flag=False
            result.append(i)
            return result
    if flag:
        result.append('Контакт не найден')
    return result

def get_all_ids(base):
    contacts=base.split('\n')
    result=[]
    for i in contacts:
        contact_data=i.split('; ')
        result.append(contact_data[0])
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
    print(contact)
    id=contact.split( )[0]
    print(id)
    index=base.index(contact)
    base[index]=id +' '+new_contact
    return base 

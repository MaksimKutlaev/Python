import csv

def add_contact(contact,all_ids):
    with open('DZ8/base.txt', 'r', encoding='utf-8') as file:
        # base=file.read()
        # c_base=base.split('\n')
        new_id=1
        id_is_create=False
        while id_is_create==False:
            if f'{new_id}' in all_ids:
                new_id+=1
            else:
                id_is_create=True
        new_contact=f'{new_id}; {contact}'
        # file.close()
        with open('DZ8/base.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n{new_contact}')
            file.close()
        with open('DZ8/base.scv', 'a', encoding='utf-8') as b:
            writer=csv.writer(b, delimiter=';')
            writer.writerows([new_contact.split('; ')])
            
            
def update_base(new_data):
    new_data_csv=[i.split(';')for i in new_data]
    with open('DZ8/base.scv','w',encoding='utf-8') as file:
         writer=csv.writer(file, delimiter=';')
         writer.writerows(new_data_csv)
    with open('DZ8/base.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_data))
            file.close()

def open_base():
    with open('DZ8/base.txt', 'r', encoding="utf-8") as base:
        return base.read()
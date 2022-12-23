import csv

def add_contact(contact):
    with open('DZ/DZ7/base.txt', 'r', encoding='utf-8') as file:
        base=file.read()
        c_base=base.split('\n')
        count=0
        for i in c_base:
            count+=1
        
        new_contact=f'{count+1}; {contact}'
        file.close()
        with open('DZ/DZ7/base.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n {new_contact}')
            file.close()
        with open('DZ/DZ7/base.scv', 'a', encoding='utf-8') as b:
            writer=csv.writer(b, delimiter=';')
            writer.writerows([new_contact.split('; ')])
            
            


def open_base():
    with open('DZ/DZ7/base.txt', 'r', encoding="utf-8") as base:
        return base.read()
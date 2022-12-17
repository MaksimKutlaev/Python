import csv
import model
import view

path = "D:/Coding/Coding/Sem151222/"

def update_base(contact):
    with open('LecFile.csv', 'w') as book:
        book.writelines(f'{contact}')
    
def del_base():
     with open('LecFile.csv', 'w') as book:
        book.writelines(f'')
    

def get_base():
    with open('LecFile.csv', 'r') as book:
        return book.readlines()
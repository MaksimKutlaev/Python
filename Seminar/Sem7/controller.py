import  model_candyes as can
import model_X_or_0 as XO
import view
from logger import win_record as log

def button_click():
    a = view.choose_game()
    if a ==1:
        res=XO.run_game()
    elif a==2:
        res=can.run_game()
    log(res)

if __name__=='__main__':
        button_click()
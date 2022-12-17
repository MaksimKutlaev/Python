from datetime import datetime as dt
from time import time

def win_record(data):
    time = dt.now().strftime('%H:%M')
    with open('Seminar/Sem7/log.txt', 'a', encoding="utf-8") as file:
        file.write('{};win;{}\n'
                    .format(time, data))


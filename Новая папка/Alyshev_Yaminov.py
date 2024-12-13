
from datetime import * 
from time import *
import time 


# Задание 1.
now = datetime.now()
custom1 = now.strftime("%d.%m.%Y");print(custom1)
custom2 = now.strftime("%d.%m.%y");print(custom2)
custom3 = now.strftime("%d %b %y");print(custom3)
custom4 = now.strftime("%d %B %y");print(custom4)
custom5 = now.strftime("%d.%m.%y - день в году : %j, неделя : %U, день недели : %A");print(custom5)
custom6 = now.strftime("Точное время : %H:%M:%S");print(custom6)
custom7 = now.strftime("Точное время (A.M) : %p %H:%M:%S ");print(custom7)

# Задание 2.
date = localtime()
dats = strftime("%A ")
month = strftime("%B")

print(f"Сегодня:\n {dats} {date.tm_mday} {month} {date.tm_year} {date.tm_hour}:{date.tm_min}:{date.tm_sec}")

# Задание 3.
def my_func():
    for i in range(1,6):
        time.sleep(3)
        print(i)
my_func()

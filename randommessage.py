import random 
import pyautogui as pg
import time
animal=('pthon','java','random')
time.sleep(8)
for i in range(21):
    a=random.choice(animal)
    pg.write(a)
    pg.press('enter')
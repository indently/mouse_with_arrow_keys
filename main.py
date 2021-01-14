import pyautogui as pg
import keyboard as k
import ctypes

user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0) / 2, user32.GetSystemMetrics(1) / 2

x = width
y = height
speed = 75

pg.moveTo(x, y)
pg.click()

while True:
    if k.is_pressed('up arrow'):
        y = y - speed
    if k.is_pressed('down arrow'):
        y = y + speed
    if k.is_pressed('left arrow'):
        x = x - speed
    if k.is_pressed('right arrow'):
        x = x + speed
    if k.is_pressed('-'):
        pg.doubleClick()

    pg.moveTo(x, y, .1)

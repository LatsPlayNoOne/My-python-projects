from win32api import Sleep
import pyautogui
import random

for i in range(100):
    cursor_pos = pyautogui.position() #get cursor pos
    jitter_x, jitter_y = random.randint(-5, 5), random.randint(-5, 5) #get new cursor pos
    pyautogui.moveTo(cursor_pos[0] + jitter_x, cursor_pos[1] + jitter_y, duration=0.1) #moving cursor to new pos
    Sleep(50)
import win32gui
import win32api
import win32con
import random
#importing some libraries.

desk = win32gui.GetDC(0) #get the first monitor and store i in our desk variable
x = win32api.GetSystemMetrics(0) #get screen width and store it in x
y = win32api.GetSystemMetrics(1) #get screen height and store it in y

for i in range(100):
    brush = win32gui.CreateSolidBrush(win32api.RGB(
        random.randrange(255), #red
        random.randrange(255), #green
        random.randrange(255), #blue
    )) #create brush for color
    win32gui.SelectObject(desk, brush)
    win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.PATINVERT)
    win32gui.DeleteObject(brush)
    win32api.Sleep(random.randrange(75))
    
    # https://www.youtube.com/watch?v=XYlhEkzkfCU
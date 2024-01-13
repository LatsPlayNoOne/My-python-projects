import win32gui
import win32api
import win32con
import random

# Get the handle of the desktop window and device context
desktop = win32gui.GetDesktopWindow()
hdc = win32gui.GetDC(desktop)

# Get screen width and height
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# If you want inf loop use "while True:"
for i in range(100): # 100 - how many
    # Generate a random color and coordinates for the line
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x1, y1 = random.randint(0, width), random.randint(0, height)
    x2, y2 = random.randint(0, width), random.randint(0, height)

    # Create a brush with the specified color
    brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
    win32gui.SelectObject(hdc, brush)

    # Draw the line
    win32gui.MoveToEx(hdc, x1, y1)
    win32gui.LineTo(hdc, x2, y2)

    # Delete the brush to release resources
    win32gui.DeleteObject(brush)

    # Sleep for a random interval
    win32api.Sleep(10)
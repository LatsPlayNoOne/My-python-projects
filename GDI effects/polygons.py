from win32con import SM_CXSCREEN, SM_CYSCREEN
from win32gui import GetDesktopWindow, GetDC, CreateSolidBrush, SelectObject, Polygon, DeleteObject
from win32api import GetSystemMetrics, RGB, Sleep
from random import randint

# Get the handle of the desktop window and device context
desktop = GetDesktopWindow()
hdc = GetDC(desktop)

# Get screen width and height using the imported function
width = GetSystemMetrics(SM_CXSCREEN)
height = GetSystemMetrics(SM_CYSCREEN)

for i in range(100):
    # Generate a random number of lines and corresponding colors and coordinates
    colors = [(randint(0, 255), randint(0, 255), randint(0, 255)) for _ in range(3)]
    points = [(randint(0, width), randint(0, height)) for _ in range(3)]

    # Create brushes with the specified colors
    brush_colors = [RGB(*color) for color in colors]
    brushes = [CreateSolidBrush(color) for color in brush_colors]
    SelectObject(hdc, brushes[0])
    
    # Draw the polygon
    Polygon(hdc, points)

    # Delete the brushes to release resources
    for brush in brushes:
        DeleteObject(brush)
    Sleep(100)

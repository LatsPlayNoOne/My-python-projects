import ctypes
import win32gui
import random

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "ඞ"]

for i in range(100):
    # Randomly generate the starting point and size of the error stripe
    x = random.randint(0, w - 1)
    y = random.randint(0, h - 1)
    stripe_width = random.randint(10, 100)

    # Randomly select an error character
    current_symbol = random.choice(symbols)

    # Draw the error stripe with the selected error character
    for i in range(stripe_width):
        win32gui.ExtTextOut(hdc, x + i * 10, y, 0, None, current_symbol, None)
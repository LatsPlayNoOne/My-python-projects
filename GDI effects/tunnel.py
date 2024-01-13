import win32api
import win32gui
import win32con

sw, sh = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
hdc = win32gui.GetDC(0)
for i in range(100):
    # Create a tunnel effect by stretching and copying the screen content
    win32gui.StretchBlt(hdc, 50, 50, sw - 100, sh - 100, hdc, 0, 0, sw, sh, win32con.SRCCOPY)
    win32api.Sleep(20) #milliseconds
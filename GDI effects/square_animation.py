import win32gui
import win32api
import win32con
import random

# Get the desktop window handle
desktop = win32gui.GetDesktopWindow()

# Initialize the initial color
current_color = win32con.WHITE_BRUSH

for i in range(1000):
    # Get the device context for the desktop
    hdc = win32gui.GetDC(desktop)

    # Set the new window dimensions
    new_width, new_height = 150, 150

    # Get the screen dimensions
    screen_width, screen_height = win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    # Generate random position for the new window
    pos_x, pos_y = random.randint(0, screen_width - new_width), random.randint(0, screen_height - new_height)

    # Create a compatible device context and bitmap
    hdc_icon = win32gui.CreateCompatibleDC(hdc)
    hbm = win32gui.CreateCompatibleBitmap(hdc, new_width, new_height)

    # Select the bitmap into the device context and fill it with the current color
    win32gui.SelectObject(hdc_icon, hbm)
    win32gui.FillRect(hdc_icon, (0, 0, new_width, new_height), current_color)

    # Copy the content of the new window to the desktop
    win32gui.BitBlt(hdc, pos_x, pos_y, new_width, new_height, hdc_icon, 0, 0, win32con.SRCCOPY)

    # Alternate the color for the next iteration
    current_color = win32con.BLACK_BRUSH if current_color == win32con.WHITE_BRUSH else win32con.WHITE_BRUSH

    # Clean up resources
    win32gui.DeleteObject(hbm)
    win32gui.DeleteDC(hdc_icon)

    # Release the desktop device context
    win32gui.ReleaseDC(desktop, hdc)

import win32gui
import win32api
import random

def create_random_square(width, height):
    size = random.randint(20, 100)
    left = random.randint(0, width - size)
    top = random.randint(0, height - size)
    return [left, top, left + size, top + size]

rectangles = [create_random_square(win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)) for _ in range(1000)]

colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(1000)]

desk = win32gui.GetDC(0)

running = True
while running:
    for i in range(len(rectangles)):
        brush = win32gui.CreateSolidBrush(win32api.RGB(*colors[i]))
        win32gui.SelectObject(desk, brush)
        win32gui.Rectangle(desk, *rectangles[i])
        win32gui.DeleteObject(brush)

        direction = random.choice(['up', 'down', 'left', 'right'])
        speed = random.randint(1, 10)

        if direction == 'up':
            rectangles[i][1] -= speed
            rectangles[i][3] -= speed
        elif direction == 'down':
            rectangles[i][1] += speed
            rectangles[i][3] += speed
        elif direction == 'left':
            rectangles[i][0] -= speed
            rectangles[i][2] -= speed
        else:
            rectangles[i][0] += speed
            rectangles[i][2] += speed

        # Ensure rectangles stay within the screen boundaries
        for j in range(4):
            if rectangles[i][j] < 0:
                rectangles[i][j] = 0
            elif j % 2 == 0 and rectangles[i][j] > win32api.GetSystemMetrics(0):
                rectangles[i][j] = win32api.GetSystemMetrics(0)
            elif j % 2 != 0 and rectangles[i][j] > win32api.GetSystemMetrics(1):
                rectangles[i][j] = win32api.GetSystemMetrics(1)

    win32api.Sleep(10)  # Delay for animation

    # You can add an exit condition here
    if len(rectangles) > 1000:
        running = False

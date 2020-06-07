import PIL.ImageDraw as ID, PIL.Image as Image
import numpy as np
import math

im = Image.new("RGB", (1000, 1000))
draw = ID.Draw(im)


def SIN(x):
    return math.sin(x * math.pi / 180)


def COS(x):
    return math.cos(x * math.pi / 180)


def draw1(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(0, 255, 0))


def draw2(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(0, 0, 255))


def draw3(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(255, 255, 255))


n = int(input("Number of Vertices in Polygon to be Rotated: "))
x = np.array([0])
x = np.empty(x)
y = np.array([0])
y = np.empty(y)
for i in range(0, n):
    x = np.append(x, input("x: "))
    y = np.append(y, input("y: "))
for i in range(0, n):
    if i == n - 1:
        draw1(int(x[i]), int(y[i]), int(x[0]), int(y[0]))
    else:
        draw1(int(x[i]), int(y[i]), int(x[i + 1]), int(y[i + 1]))
angle = int(input("Rotation Angle: "))
x_pivot = int(input("Rotation Point X: "))
y_pivot = int(input("Rotation Point Y: "))
for i in range(0, n):
    draw3(int(x_pivot), int(y_pivot), int(x[i]), int(y[i]))
for i in range(0, n):
    x_shifted = x[i] - x_pivot
    y_shifted = y[i] - y_pivot
    x[i] = x_pivot + (x_shifted * COS(angle) - y_shifted * SIN(angle));
    y[i] = y_pivot + (x_shifted * SIN(angle) + y_shifted * COS(angle));
for i in range(0, n):
    if i == n - 1:
        draw2(int(x[i]), int(y[i]), int(x[0]), int(y[0]))
    else:
        draw2(int(x[i]), int(y[i]), int(x[i + 1]), int(y[i + 1]))
for i in range(0, n):
    draw3(int(x_pivot), int(y_pivot), int(x[i]), int(y[i]))

im.show()

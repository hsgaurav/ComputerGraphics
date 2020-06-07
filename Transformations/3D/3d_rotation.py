import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS
from matplotlib import pyplot as plt
import numpy as np
import math

im = Image.new("RGB", (1000,1000))
draw = ID.Draw(im)

def SIN(x):
    return math.sin(x * math.pi/180)

def COS(x):
    return math.cos(x * math.pi/180)

def draw1(x1, y1, x2, y2):
    draw.line((x1,y1,x2,y2),fill=(0,255,0))

def draw2(x1, y1, x2, y2):
    draw.line((x1,y1,x2,y2),fill=(0,0,255))

def draw3(x1, y1, x2, y2):
    draw.line((x1,y1,x2,y2),fill=(255,255,255))

n = 4
x = np.array([500,600,600,500,450,550,550,450])
y = np.array([500,500,600,600,450,450,550,550])

for i in range(0,n):
    if i == n - 1:
        draw1(int(x[i]),int(y[i]),int(x[0]),int(y[0]))
    else:
        draw1(int(x[i]),int(y[i]),int(x[i+1]),int(y[i+1]))

for i in range(0,n):
    if i == n - 1:
        draw1(int(x[i+4]),int(y[i+4]),int(x[4]),int(y[4]))
    else:
        draw1(int(x[i+4]),int(y[i+4]),int(x[i+5]),int(y[i+5]))


for i in range(0,n):
    draw1(int(x[i]),int(y[i]),int(x[i+4]),int(y[i+4]))

angle = int(input("Rotation Angle: "))
x_pivot = int(input("Rotation Point X: "))
y_pivot = int(input("Rotation Point Y: "))

for i in range(0,n*2):
    draw3(int(x_pivot),int(y_pivot),int(x[i]),int(y[i]))
    
for i in range(0,n*2):
    x_shifted = x[i] - x_pivot
    y_shifted = y[i] - y_pivot
    x[i] = x_pivot + (x_shifted*COS(angle) - y_shifted*SIN(angle));
    y[i] = y_pivot + (x_shifted*SIN(angle) + y_shifted*COS(angle));


for i in range(0,n):
    if i == n - 1:
        draw2(int(x[i]),int(y[i]),int(x[0]),int(y[0]))
    else:
        draw2(int(x[i]),int(y[i]),int(x[i+1]),int(y[i+1]))


for i in range(0,n):
    if i == n - 1:
        draw2(int(x[i+4]),int(y[i+4]),int(x[4]),int(y[4]))
    else:
        draw2(int(x[i+4]),int(y[i+4]),int(x[i+5]),int(y[i+5]))


for i in range(0,n):
    draw2(int(x[i]),int(y[i]),int(x[i+4]),int(y[i+4]))

for i in range(0,n*2):
    draw3(int(x_pivot),int(y_pivot),int(x[i]),int(y[i]))
        
im.show();

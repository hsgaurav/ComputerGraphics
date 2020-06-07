import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS
from matplotlib import pyplot as plt
import numpy as np

im = Image.new("RGB", (1000,1000))
draw = ID.Draw(im)

def draw1(x1, y1, x2, y2):
    draw.line((x1,y1,x2,y2),fill=(0,255,0))

def draw2(x1, y1, x2, y2):
    draw.line((x1,y1,x2,y2),fill=(0,0,255))

n = 4
x = np.array([100,200,200,100,50,150,150,50])
y = np.array([100,100,200,200,50,50,150,150])

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

sx = int(input("X-axis Scaling: "))
sy = int(input("Y-axis Scaling: "))
    
for i in range(0,n*2):
    x[i] = x[i] * sx
    y[i] = y[i] * sy


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
        
im.show();

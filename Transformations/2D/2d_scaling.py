import PIL.ImageDraw as ID, PIL.Image as Image
import numpy as np

im = Image.new("RGB", (1000,1000))
draw = ID.Draw(im)


def draw1(x1, y1, x2, y2):
    draw.line((x1,y1,x2,y2),fill=(0,255,0))


def draw2(x1, y1, x2, y2):
    draw.line((x1,y1,x2,y2),fill=(0,0,255))

n = int(input("Number of Vertices in Polygon to be Scaled: "))
x = np.array([0])
x = np.empty(x)
y = np.array([0])
y = np.empty(y)
for i in range(0,n):
    x = np.append(x, input("x: "))
    y = np.append(y, input("y: "))

for i in range(0,n):
    if i == n-1:
        draw1(int(x[i]),int(y[i]),int(x[0]),int(y[0]))
    else:
        draw1(int(x[i]),int(y[i]),int(x[i+1]),int(y[i+1]))
sx = int(input("X-axis Scaling: "))
sy = int(input("Y-axis Scaling: "))
for i in range(0,n):
    x[i] = x[i] * sx
    y[i] = y[i] * sy
for i in range(0,n):
    if i == n-1:
        draw2(int(x[i]),int(y[i]),int(x[0]),int(y[0]))
    else:
        draw2(int(x[i]),int(y[i]),int(x[i+1]),int(y[i+1]))
        
im.show()

import PIL.ImageDraw as ID, PIL.Image as Image


def draw1(x1, y1):
    draw.point((x1, y1), fill=(0, 255, 0))


def drawCircle(xc, yc, x, y):
    draw1(xc + x, yc + y)
    draw1(xc - x, yc + y)
    draw1(xc + x, yc - y)
    draw1(xc - x, yc - y)
    draw1(xc + y, yc + x)
    draw1(xc - y, yc + x)
    draw1(xc + y, yc - x)
    draw1(xc - y, yc - x)


def bresenhamCircleDraw(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    drawCircle(xc, yc, x, y)
    while y >= x:
        x = x + 1
        if d > 0:
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y)


if __name__ == '__main__':
    im = Image.new("RGB", (640, 480))
    draw = ID.Draw(im)
    x = int(input("x-coordinate of centre: "))
    y = int(input("y-coordinate of centre: "))
    r = int(input("Radius: "))
    bresenhamCircleDraw(x, y, r)
    im.show()

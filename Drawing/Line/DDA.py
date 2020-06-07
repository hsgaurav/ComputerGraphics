import PIL.ImageDraw as ID, PIL.Image as Image


def draw1(x1, y1):
    draw.point((x1, y1), fill=(0, 255, 0))


def ROUND(a):
    return int(a + 0.5)


def drawDDA(x1, y1, x2, y2):
    x, y = x1, y1
    length = (x2 - x1) if (x2 - x1) > (y2 - y1) else (y2 - y1)
    dx = (x2 - x1) / float(length)
    dy = (y2 - y1) / float(length)
    for i in range(length):
        x += dx
        y += dy
        x1 = ROUND(x)
        y1 = ROUND(y)
        draw1(x1, y1)
    im.show()


if __name__ == '__main__':
    im = Image.new("RGB", (640, 480))
    draw = ID.Draw(im)
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    drawDDA(x1, y1, x2, y2)

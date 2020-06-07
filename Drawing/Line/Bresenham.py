import PIL.ImageDraw as ID, PIL.Image as Image


def draw1(x1, y1):
    draw.point((x1, y1), fill=(0, 255, 0))


def ROUND(a):
    return int(a + 0.5)


def drawBresenham(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        p = 2 * (abs(dy)) - (abs(dx))
        y = y1
        x = x1
        for i in range(0, abs(dx) + 1):
            draw1(x, y)
            if p >= 0:
                y = y + 1 if dy >= 0 else y - 1
                p = p + 2*abs(dy) - 2*abs(dx)
            else:
                p = p + 2*abs(dy)
            x = x + 1 if dx >= 0 else x - 1
    else:
        p = 2 * (abs(dx)) - (abs(dy))
        x = x1
        y = y1
        for i in range(0 , abs(dy) + 1):
            draw1(x, y)
            if p >= 0:
                x = x + 1 if dx >= 0 else x - 1
                p = p + 2*abs(dx) - 2*abs(dy)
            else:
                p = p + 2*abs(dx)
            y = y + 1 if dy >= 0 else y - 1
    im.show()


if __name__ == '__main__':
    im = Image.new("RGB", (640, 480))
    draw = ID.Draw(im)
    drawBresenham(200, 500, 500, 200)

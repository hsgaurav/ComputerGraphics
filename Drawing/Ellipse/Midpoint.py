import PIL.ImageDraw as ID, PIL.Image as Image


def draw1(x1, y1):
    draw.point((x1, y1), fill=(0, 255, 0))


def midptellipse(rx, ry, xc, yc):
    x = 0
    y = ry
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    while dx < dy:
        draw1(x + xc, y + yc)
        draw1(-x + xc, y + yc)
        draw1(x + xc, -y + yc)
        draw1(-x + xc, -y + yc)
        if d1 < 0:
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))
    while y >= 0:
        draw1(x + xc, y + yc)
        draw1(-x + xc, y + yc)
        draw1(x + xc, -y + yc)
        draw1(-x + xc, -y + yc)
        if d2 > 0:
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)


if __name__ == '__main__':
    im = Image.new("RGB", (640, 480))
    draw = ID.Draw(im)
    x = int(input("x-coordinate of centre: "))
    y = int(input("y-coordinate of centre: "))
    r1 = int(input("Major Radius: "))
    r2 = int(input("Minor Radius: "))
    midptellipse(r1, r2, x, y)
    im.show()

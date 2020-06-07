# Line Clipping Using LiangBarsky Algorithm

import PIL.ImageDraw as ID, PIL.Image as Image


def roundno(a):
    return int(a + 0.5)


def cliptest(p, q, t1, t2):
    retVal = 1

    if p < 0.0:
        r = float(q) / float(p)
        if r > t2[0]:
            retVal = 0
        elif r > t1[0]:
            t1[0] = r
    elif p > 0.0:
        r = float(q) / float(p)
        if r < t1[0]:
            retVal = 0
        elif r < t2[0]:
            t2[0] = r

    elif q < 0.0:
        retVal = 0

    return retVal


def lbclipLine(x1, y1, x2, y2):
    t1 = [0.0]
    t2 = [1.0]
    dx = x2 - x1
    if cliptest(-dx, x1 - winMinX, t1, t2):
        if cliptest(dx, winMaxX - x1, t1, t2):
            dy = y2 - y1
            if cliptest(-dy, y1 - winMinY, t1, t2):
                if cliptest(dy, winMaxY - y1, t1, t2):
                    if t2[0] < 1.0:
                        x2 = x1 + t2[0] * dx
                        y2 = y1 + t2[0] * dy

                    if t1[0] > 0.0:
                        x1 = x1 + t1[0] * dx
                        y1 = y1 + t1[0] * dy
                    draw2.line((roundno(x1), roundno(y1), roundno(x2), roundno(y2)), fill=(0, 255, 0))


def clip(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(0, 255, 0))
    lbclipLine(x1, y1, x2, y2)


if __name__ == '__main__':
    im = Image.new("RGB", (640, 480))
    im1 = Image.new("RGB", (640, 480))
    draw = ID.Draw(im)
    draw2 = ID.Draw(im1)
    draw.polygon((200, 200, 400, 200, 400, 300, 200, 300), outline=255)
    draw2.polygon((200, 200, 400, 200, 400, 300, 200, 300), outline=255)
    winMinX = 200
    winMaxX = 400
    winMinY = 200
    winMaxY = 300
    t1 = [0.0]
    t2 = [1.0]
    x1 = 290
    y1 = 130
    x2 = 220
    y2 = 400
    clip(x1, y1, x2, y2)
    im.show()
    im1.show()

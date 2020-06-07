import PIL.ImageDraw as ID, PIL.Image as Image


def draw1(x1, y1):
    draw.point((x1, y1), fill=(0, 255, 0))


def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0
    draw1(x + x_centre, y + y_centre)
    if r > 0:
        draw1(x + x_centre, -y + y_centre)
        draw1(y + x_centre, x + y_centre)
        draw1(-y + x_centre, x + y_centre)
    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if x < y:
            break
        draw1(x + x_centre, y + y_centre)
        draw1(-x + x_centre, y + y_centre)
        draw1(x + x_centre, -y + y_centre)
        draw1(-x + x_centre, -y + y_centre)
        if x != y:
            draw1(y + x_centre, x + y_centre)
            draw1(-y + x_centre, x + y_centre)
            draw1(y + x_centre, -x + y_centre)
            draw1(-y + x_centre, -x + y_centre)


if __name__ == '__main__':
    im = Image.new("RGB", (640, 480))
    draw = ID.Draw(im)
    x = int(input("x-coordinate of centre: "))
    y = int(input("y-coordinate of centre: "))
    r = int(input("Radius: "))
    midPointCircleDraw(x, y, r)
    im.show()

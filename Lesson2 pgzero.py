import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300


def draw():
    r = 255
    g = 0
    b = randint(120, 255)

    width = 100
    height = 100 

    for i in range(20):
        rect = Rect((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r, g, b))

        r -= 10
        g += 10

        width -= 10
        height -= 10


pgzrun.go()
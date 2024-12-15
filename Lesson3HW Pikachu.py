import pgzrun
from random import randint

TITLE ="Good shot"
WIDTH=500
HEIGHT=500

message=""

alien = Actor("pikachu")

def draw():
    screen.clear()
    screen.fill(color=(128,200,0))
    alien.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)

def place_alien():
    alien.x=randint(50,WIDTH-50)
    alien.y=randint(50,WIDTH-50)

def on_mouse_down(pos):
    #print("Hello world")
    if alien.collidepoint(pos):
        message="Good shot"
        print(message)
        place_alien()
    else:
        message="You missed"
        print(message)

place_alien()
pgzrun.go()
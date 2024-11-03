import pgzrun
import random

WIDTH=  600
HEIGHT= 400

no_of_sats=0
sats=[]
lines=[]
next=0
for i in range(10):
    satellite=Actor("satellite")
    satellite.x=random.randint(50,WIDTH-50)
    satellite.y=random.randint(50,HEIGHT-50)
    sats.append(satellite)



def draw ():
    numbers=1
    screen.blit("spacebg",(0,0))

    for i in sats:
        i.draw()
        screen.draw.text(str(numbers),(i.x,i.y+15),color="cyan")
        numbers+=1
    for line in lines:
        screen.draw.line(line[0],line[1],color="red")

def on_mouse_down(pos):
    global sats,lines,next
    if sats [next].collidepoint(pos):
        if next:
            lines.append((sats[next-1].pos,sats[next].pos))
        next+=1
    else:
        lines=[]
        next=0


pgzrun.go()


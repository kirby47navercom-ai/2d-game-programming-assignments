from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
while True:
    while x<780:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.001)
    while y<560:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=2
        delay(0.001)
    while x>20:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=2
        delay(0.001)
    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=2
        delay(0.001)
    while x<400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.001)
    r=270
    while r>=-90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+210*math.cos(r/360*2*math.pi),300+210*math.sin(r/360*2*math.pi))
        r-=2
        delay(0.01)


close_canvas()
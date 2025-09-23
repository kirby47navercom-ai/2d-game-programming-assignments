from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('girl_nuki-Photoroom.png')

def sprite_run():
    frame = 0
    for x in range(40):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(10+frame*57, 730,55, 100,400, 300,200,200)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
    pass


while True:
    sprite_run()





close_canvas()
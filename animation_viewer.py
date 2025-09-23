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
def sprite_sideattack():
    for x in range(5):
        frame = 0
        for y in range(4):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(5+frame * 58, 640, 57, 90, 400, 300, 200, 200)
            update_canvas()
            frame = (frame + 1)
            delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5 + frame * 58, 640, 90, 90, 400, 300, 300, 200)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5 + frame * 64, 640, 90, 90, 400, 300, 300, 200)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5 + frame * 67, 640, 87, 90, 400, 300, 300, 200)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5 + frame * 70, 640, 87, 90, 400, 300, 200, 200)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)
    pass

def sprite_downattack():
    frame = 0
    for x in range(20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5+frame * 50, 553, 50, 78, 400, 300, 200, 200)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.1)
    pass
def sprite_jump():
    frame = 0
    for x in range(20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 50, 480, 50, 78, 400, 300, 200, 200)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.1)
    pass
def sprite_spinattack():
    pass
while True:
    # sprite_run()
    # delay(1)
    # sprite_sideattack()
    # delay(1)
    # sprite_downattack()
    # delay(1)
    #sprite_jump()
    #delay(1)
    sprite_spinattack()
    delay(1)



close_canvas()
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('girl_nuki-Photoroom.png')

def sprite_run():
    frame = 0
    for x in range(40):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(10+frame*57, 730,55, 100,400, 300,200*2,200*2)
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
            character.clip_draw(5+frame * 58, 640, 57, 90, 400+y*10, 300, 200*2, 200*2)
            update_canvas()
            frame = (frame + 1)
            delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(7 + frame * 58, 640, 90, 90, 440, 300, 300*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(6 + frame * 64, 640, 90, 90, 450, 300, 300*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5 + frame * 67, 640, 87, 90, 460, 300, 300*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5 + frame * 70, 640, 87, 90, 470, 300, 200*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)
    pass

def sprite_downattack():
    frame = 0
    for x in range(20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(5+frame * 50, 553, 50, 78, 400, 300, 200*2, 200*2)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.1)
    pass
def sprite_jump():
    frame = 0
    for x in range(20):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 50, 480, 50, 78, 400+(x%5)*10, 300, 200*2, 200*2)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.1)
    pass
def sprite_spinattack():
    for x in range(5):
        frame = 0
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 65, 246, 59, 78, 300, 300, 220*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 65, 246, 65, 78, 360, 300, 220*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 65, 246, 55, 78, 400, 300, 200*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 65-18, 246, 55+70, 78, 470, 300, 400*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(40+frame * 65, 246, 55+30, 78, 560, 300, 300*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 95, 246, 55 + 30, 78, 540, 300, 300*2, 200*2)
        update_canvas()
        frame = (frame + 1)
        delay(0.1)
    pass
while True:
    sprite_run()
    delay(1)
    sprite_sideattack()
    delay(1)
    sprite_downattack()
    delay(1)
    sprite_jump()
    delay(1)
    sprite_spinattack()
    delay(1)



close_canvas()
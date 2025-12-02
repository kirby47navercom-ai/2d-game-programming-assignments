import random
from pico2d import load_image
import common

class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(300,1500)
        self.y = random.randint(300,800)


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x-common.court.window_left,self.y-common.court.window_bottom)



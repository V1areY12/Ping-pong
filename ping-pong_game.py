from pygame import *
from time import time as timer


win_width = 900
win_height =  700

BACK = (200,255,255)
win = display.set_mode((win_width, win_height))
display.set_caption('Пинг понг')
background = image.load('FONN.jpg')
background = transform.scale(background, ( win_width ,win_height))
image_ball = image.load('balll.png')
image_ball = transform.scale(image_ball, (75,75))
image_racket = image.load('platform.png')
image_racket = transform.scale(image_racket, (25, 100))

font.init()
font_goal = font.SysFont('Arial', 40)
font_time = font.SysFont('Arial', 28)

clock = time.Clock
FPS = 60

class Gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = image_load(img)
        self.img = transform_scale(self.image, (win_windth, win_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
    
class Right(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed

class Left(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 600:
            self.rect.y += self.speed

class Ball(Gamesprite):
    def update(self):
        self.rect.x = self.rect.x + self.speed * speed_x
        self.rect.y = self.rect.y + self.speed * speed_y

        if self.rect.y > win_height or self.rect.y < 0:
            speed_y *= -1

        


        
from pygame import *
from time import time as timer


win_width = 900
win_height =  700
speed_x = 3
speed_y = 3

BACK = (200,255,255)
win = display.set_mode((win_width, win_height))
display.set_caption('Пинг понг')




font.init()
font_goal = font.SysFont('Arial', 40)
font_time = font.SysFont('Arial', 28)
lose_right = font_goal.render(' PLAYER LEFT WIN!', True, (180,0,0))
lose_left = font_goal.render(' PLAYER RIGHT WIN!', True, (180,0,0))
goal_right = 0
goal_left = 0

clock = time.Clock()
FPS = 60

class Gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = image.load(img)
        self.img = transform.scale(self.image, (win_width, win_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

    
    def colliderect(self, block):
        return sprite.collide_rect(self, block)
    
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
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed



ball = Gamesprite('balll.png', 425, 325, 50, 50, 4)
racket_1 = Right('platform.png', 860, 300, 30, 100, 4 )
racket_2 = Left('platform.png', 10, 300, 30, 100, 4 )
game = True
finish = False
start_time = timer()
while game:
    current_time = timer()
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        win.fill(BACK)
        racket_1.update()
        racket_2.update()
        ball.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if ball.rect.y > 640 or ball.rect.y < 10:
            speed_y *= -1

        if ball.colliderect ( racket_1) or ball.colliderect( racket_2):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.x < 10:
            goal_right += 15
            ball.rect.x = 425
            ball.rect.y = 325
            time.delay(500)
        
        if ball.rect.x > 840:
            goal_left += 15
            ball.rect.x = 425
            ball.rect.y = 325
            time.delay(500)
        

        check_left = font_time.render(str(goal_left), True, (0,0,0))
        check_right = font_time.render(str(goal_right), True, (0,0,0))
        ckeck_DOT = font_time.render(' - ', True, (0, 0, 0))
        win.blit(check_left, (445 ,25))
        win.blit(check_right, ( 485 ,25))


        if goal_right > 45:
            win.blit(lose_left, (200, 300))
            finish = True
        
        if goal_left > 45:
            win.blit(lose_right, (200, 300))
            finish = True

        racket_1.reset()
        racket_2.reset()
        ball.reset()


        if current_time - start_time > 30:
            start_time = timer()
            speed_x += 1
            speed_y += 1

    else:
        start_time = timer()
        time.delay(3000)
        ball.rect.x = 425
        ball.rect.y = 325
        racket_1.rect.y = 300
        racket_2.rect.y = 300
        goal_right = 0
        goal_left = 0
        finish = False
               



    
    display.update()
    clock.tick(FPS)

        


        
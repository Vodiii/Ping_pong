from pygame import *
class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>5:
            self.rect.y -=self.speed
        if keys_pressed[K_s] and self.rect.y>-80: 
            self.rect.y +=self.speed 
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)
FPS = 60 
game = True
finish = False
clock = time.Clock()
racket1 = Player('racketka.png',30,200,4,50,150)
racket2 = Player('racketka.png',30,200,4,50,150)
ball = GameSprite('Mach dla python.png',200,200,4,50,50)
while game:
    for e in event.get():
        if e.type ==QUIT:
            game = False


    display.update()

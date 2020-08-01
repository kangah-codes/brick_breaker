import pygame
import math
import random
from config.settings import *
pygame.mixer.pre_init(44100, 16, 2, 4096) #
pygame.init()

screen = pygame.display.set_mode((800, 500))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "07-Breakout-Tiles.png"))), (80, 20))
        self.pos = pygame.math.Vector2()
        self.pos.x = 100
        self.pos.y = 450
        self.speed = 15
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.current_image = None
        self.dt = clock.tick(fps)*0.001
        self.moving = False
        self.gameOver = False
        self.life = 4

    def update(self, dt):
        self.rect.x = self.pos.x 
        self.rect.y = self.pos.y
        self.mask = pygame.mask.from_surface(self.image)
        if self.pos.x - self.rect.width > 700:
            self.pos.x = 0 - self.rect.width
        if self.pos.x + self.rect.width < 0:
            self.pos.x = 700 + self.rect.width

        try:
            keyPress = pygame.key.get_pressed()

            if keyPress[pygame.K_a]:
                self.moving = True
                self.pos.x -= self.speed
            if keyPress[pygame.K_d]:
                self.moving = True
                self.pos.x += self.speed
            if not keyPress[pygame.K_a] and not keyPress[pygame.K_d]:
                self.moving = False

        except:
            pass

        if self.life <= 0:
            self.life = 5
            gameOver()

    def draw(self, display):
        try:
            display.blit(self.image, (self.pos.x, self.pos.y))
        except:
            pass

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(random.choice(brick_images), (80, 40))
        self.pos = pygame.math.Vector2()
        self.pos.x = x
        self.pos.y = y
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.bounceSpeed = speed

    def update(self):
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        collided_bricks = pygame.sprite.groupcollide(brickGroup, ballGroup, True, False, pygame.sprite.collide_mask)
        if collided_bricks:
            ballGroup.sprites()[0].flipY()

    def draw(self, display):
        try:
            display.blit(self.image, (self.pos.x, self.pos.y))
        except:
            pass

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "58-Breakout-Tiles.png"))), (25, 25))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2()
        self.pos.x = random.randint(0, 800-self.rect.width)
        self.pos.y = 150
        self.xspeed = speed
        self.yspeed = speed

    def flipY(self):
        self.yspeed *= -1

    def flipX(self):
        self.xspeed *= -1

    def update(self, player):
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y 
        self.pos.y += self.yspeed
        self.pos.x += self.xspeed

        if pygame.sprite.collide_mask(self, player):
            #self.pos.y -= random.choice([1,2,3])
            self.yspeed = -speed
            if player.moving:
                self.xspeed = self.flipX()

        if self.pos.y + self.rect.height >= 500 or self.pos.y <= 0:
            self.flipY()

        if self.pos.y + self.rect.height >= 500:
            player.life -= 1

        if self.pos.x + self.rect.width >= 800 or self.pos.x <= 0:
            self.flipX()

    def draw(self, display):
        try:
            display.blit(self.image, (self.pos.x, self.pos.y))
        except:
            pass
        


import pygame
import math
import random
from fading import *
pygame.mixer.pre_init(44100, 16, 2, 4096) #
pygame.init()

screen = pygame.display.set_mode((800, 500))

clock = pygame.time.Clock()

fps = 60

brick_images = [
    pygame.image.load("PNG/01-Breakout-Tiles.png"),
    pygame.image.load("PNG/03-Breakout-Tiles.png"),
    pygame.image.load("PNG/05-Breakout-Tiles.png"),
    pygame.image.load("PNG/07-Breakout-Tiles.png"),
    pygame.image.load("PNG/09-Breakout-Tiles.png"),
    pygame.image.load("PNG/11-Breakout-Tiles.png"),
]

brickGroup = pygame.sprite.Group()
ballGroup = pygame.sprite.Group()

speed = 5
gameover = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("PNG/07-Breakout-Tiles.png"), (80, 20))
        #self.image = pygame.image.load("PNG/49-Breakout-Tiles.png")
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
        #print(self.rect.x)
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
        ball = ballGroup.sprites()[0]
        if pygame.sprite.collide_mask(self, ball):
            if ball.rect.right >= self.rect.left:
                ball.xspeed = -self.bounceSpeed
                self.kill()
            if ball.rect.left <= self.rect.right:
                ball.xspeed = self.bounceSpeed
                self.kill()
            if ball.rect.bottom >= self.rect.top:
                ball.yspeed = -self.bounceSpeed
                self.kill()
            if ball.rect.top <= self.rect.bottom:
                ball.yspeed = self.bounceSpeed
                self.kill()



    def draw(self, display):
        try:
            display.blit(self.image, (self.pos.x, self.pos.y))
        except:
            pass

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("PNG/58-Breakout-Tiles.png"), (25, 25))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2()
        self.pos.x = random.randint(0, 800-self.rect.width)
        self.pos.y = 150
        self.xspeed = speed
        self.yspeed = speed

    def update(self, player):
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y 
        #print(self.yspeed)
        self.pos.y += self.yspeed
        self.pos.x += self.xspeed

        if pygame.sprite.collide_mask(self, player):
            #self.pos.y -= random.choice([1,2,3])
            self.yspeed = -random.choice([3,4,5,6])
            if player.moving:
                self.xspeed = -random.choice([3,4,5,6])

        if self.pos.y + self.rect.height >= 500 or self.pos.y <= 0:
            self.yspeed *= -1

        if self.pos.y + self.rect.height >= 500:
            player.life -= 1
            #print("Above")

        if self.pos.x + self.rect.width >= 800 or self.pos.x <= 0:
            self.xspeed *= -1

    def draw(self, display):
        try:
            display.blit(self.image, (self.pos.x, self.pos.y))
        except:
            pass
        
level = 0

running = True
allowNew = False

player = Player()
ballGroup.add(Ball())

levelText = FadingText(f"Level {level}", [255,255,255], 64, .3)
showOnce = True
contRender = False

main_font = levelText.font.render("Brick Breaker", True, (255,255,255))
start = levelText.font1.render("Press A to start", True, (0,255,0))
quitg = levelText.font1.render("Press Q to quit", True, (255,0,0))

game_over = levelText.font.render("Game Over!", True, (255, 0 ,0))
score = levelText.font1.render(f"Your reached level {level}", True, (255,0,0))

green = (0,255,0)
red = (255,0,0)
orange = (255,165,0)
color = green

pygame.mixer.music.load('retro.mp3')
pygame.mixer.music.play(-1)

refresh = False

def mainMenu():
    player.gameOver = False
    global running
    running = True
    while running:
        #print(player.gameOver)
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pygame.mixer.music.pause()
                        game()
                        #running = False
                    if event.key == pygame.K_q:
                        running = False
           
            screen.fill((0, 0, 0))

            screen.blit(main_font, (118, 100))
            screen.blit(start, (400 - (start.get_width()/2), 200))
            screen.blit(quitg, (400 - (quitg.get_width()/2), 250))

            pygame.display.update()

            clock.tick(20)

        except:
            pass

def gameOver():
    global running
    global level
    if player.life <= 0:
        while running:
            score = levelText.font1.render(f"You  reached level {level}", True, (255,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            try:
                screen.fill((0, 0, 0))

                screen.blit(game_over, (400 - game_over.get_width()/2, 100))
                screen.blit(score, (400 - (score.get_width()/2), 200))

                pygame.display.update()

                pygame.time.wait(2000)
                running = False
                refresh = True
                level = 0
                for brick in brickGroup:
                    brick.kill()
                mainMenu()

                clock.tick(20)

            except:
                pass
    else:
        while running:
            score = levelText.font1.render(f"You  reached level {level}", True, (255,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            try:
                screen.fill((0, 0, 0))

                screen.blit(game_over, (400 - game_over.get_width()/2, 100))
                screen.blit(score, (400 - (score.get_width()/2), 200))

                pygame.display.update()

                pygame.time.wait(2000)
                running = False
                refresh = True
                mainMenu()

                clock.tick(20)

            except:
                pass
            level = 0
            for brick in brickGroup:
                brick.kill()
            print(len(brickGroup))
            mainMenu()

def game():
    #pygame.mixer.pause()
    global running
    global showOnce
    global level
    global speed
    global color
    global contRender
    global refresh
    running = True
    switch = True

    while running:
        life = levelText.font1.render(f"Life: {player.life}", True, color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        try:
            screen.fill((0, 0, 0))
            screen.blit(life, (0, 500 - life.get_height()))

            if player.life >= 3:
                color = green
            elif player.life == 2:
                color = orange
            else:
                color = red

        except:
            pass

        player.update(player.dt)
        brickGroup.update()
        ballGroup.update(player)

        player.draw(screen)

        if showOnce:
            levelText.render()
            levelText.fade(screen, 300, 200)

            if levelText.alpha == 0:
                showOnce = False

        try:
            brickGroup.draw(screen)
            ballGroup.draw(screen)
            pygame.display.update()

        except:
            pass

        
        #print(len(bri))

        if switch:
            refresh = True
            switch = False

        if refresh:
            for brick in brickGroup:
                brick.kill()
            for i in range(800):
                for y in range(level*40):
                    if i % 80 == 0 and y % 40 == 0:
                        brickGroup.add(Brick(i, y))
            refresh = False


        if len(brickGroup) == 0:
            #print(level)
            #print("lesser")
            levelText.alpha = 255
            contRender = True
            level += 1
            speed += 1
            player.speed -= 1.5
            player.life += 1
            ball = ballGroup.sprites()[0]
            ball.pos.x = 400 - ball.rect.width/2
            ball.pos.y = 400
            
            for i in range(800):
                for y in range(level*40):
                    if i % 80 == 0 and y % 40 == 0:
                        brickGroup.add(Brick(i, y))
            
            levelText.text = f"Level {level}"
        
        #global contRender
        if contRender:
            levelText.render()
            levelText.fade(screen, 300, 200)

            if levelText.alpha <= 0:
                contRender = False

        # global gameover

        #print(gameover)

        clock.tick(fps)



mainMenu()

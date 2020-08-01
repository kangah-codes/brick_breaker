import os
import pygame

# base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# global game settings
FPS = 60
level = 0

running = True
allowNew = False

green = (0,255,0)
red = (255,0,0)
orange = (255,165,0)
color = green

refresh = False

brickGroup = pygame.sprite.Group()
ballGroup = pygame.sprite.Group()

clock = pygame.time.Clock()

fps = 60


brick_images = [
    pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "01-Breakout-Tiles.png"))),
    pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "03-Breakout-Tiles.png"))),
    pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "05-Breakout-Tiles.png"))),
    pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "07-Breakout-Tiles.png"))),
    pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "09-Breakout-Tiles.png"))),
    pygame.image.load(os.path.join(BASE_DIR, os.path.join("assets", "11-Breakout-Tiles.png")))
]

speed = 5
gameover = False

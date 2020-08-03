import os
import pygame
import random

# base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# scale factor for all our sprites

SCALE = 0.25

FPS = 60

# deltatime variable
DT = FPS * 0.00005

clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500

"""
Difficulty Levels:
1 = Easy
2 = Normal
3 = Hard
4 = Impossible
"""

DIFFICULTY = 1
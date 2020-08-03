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

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 500

# load player sprites
player_sprites = {
	'healthy': [
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/50-Breakout-Tiles.png')),
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/51-Breakout-Tiles.png')),
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/52-Breakout-Tiles.png')),
	],
	'shrunk': [
		# using a lambda function with image as an argument to prevent us from calling pygame.image.load to replare all occurences of image
		(lambda image : pygame.transform.scale(
			image,
			(int(image.get_rect().width * SCALE), int(image.get_rect().height * SCALE))
		))(pygame.image.load(os.path.join(BASE_DIR, 'assets/player/57-Breakout-Tiles.png')))
	],
	'slow': [
		# using a lambda function with image as an argument to prevent us from calling pygame.image.load to replare all occurences of image
		(lambda image : pygame.transform.scale(
			image,
			(int(image.get_rect().width * SCALE), int(image.get_rect().height * SCALE))
		))(pygame.image.load(os.path.join(BASE_DIR, 'assets/player/41-Breakout-Tiles.png')))
	],
	'fast': [
		# using a lambda function with image as an argument to prevent us from calling pygame.image.load to replare all occurences of image
		(lambda image : pygame.transform.scale(
			image,
			(int(image.get_rect().width * SCALE), int(image.get_rect().height * SCALE))
		))(pygame.image.load(os.path.join(BASE_DIR, 'assets/player/42-Breakout-Tiles.png')))
	]
}
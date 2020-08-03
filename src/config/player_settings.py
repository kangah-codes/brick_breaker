from .settings import *

# player variables
NORMAL_SPEED = 8
SLOW_SPEED = 3.5
FAST_SPEED = 10
Y_LOCATION = 450

# load player sprites
player_sprites = {
	'healthy': [
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/50-Breakout-Tiles.png')),
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/51-Breakout-Tiles.png')),
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/52-Breakout-Tiles.png')),
	],
	'laser': [
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/53-Breakout-Tiles.png')),
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/54-Breakout-Tiles.png')),
		pygame.image.load(os.path.join(BASE_DIR, 'assets/player/55-Breakout-Tiles.png')),
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
	],
	'kill_row': [
		# this state removes a whole row of blocks when a player hits it with the ball
		# using a lambda function with image as an argument to prevent us from calling pygame.image.load to replare all occurences of image
		(lambda image : pygame.transform.scale(
			image,
			(int(image.get_rect().width * SCALE), int(image.get_rect().height * SCALE))
		))(pygame.image.load(os.path.join(BASE_DIR, 'assets/player/48-Breakout-Tiles.png')))
	],
	'strength_1': [
		# using a lambda function with image as an argument to prevent us from calling pygame.image.load to replare all occurences of image
		(lambda image : pygame.transform.scale(
			image,
			(int(image.get_rect().width * SCALE), int(image.get_rect().height * SCALE))
		))(pygame.image.load(os.path.join(BASE_DIR, 'assets/player/45-Breakout-Tiles.png')))
	],
	'strength_2': [
		# using a lambda function with image as an argument to prevent us from calling pygame.image.load to replare all occurences of image
		(lambda image : pygame.transform.scale(
			image,
			(int(image.get_rect().width * SCALE), int(image.get_rect().height * SCALE))
		))(pygame.image.load(os.path.join(BASE_DIR, 'assets/player/44-Breakout-Tiles.png')))
	],
	'hold': [
		# using a lambda function with image as an argument to prevent us from calling pygame.image.load to replare all occurences of image
		(lambda image : pygame.transform.scale(
			image,
			(int(image.get_rect().width * SCALE), int(image.get_rect().height * SCALE))
		))(pygame.image.load(os.path.join(BASE_DIR, 'assets/player/43-Breakout-Tiles.png')))
	],
}
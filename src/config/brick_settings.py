from .settings import *

BRICK_WIDTH = 80
BRICK_HEIGHT = 40

# spritegroup for bricks
brick_group = pygame.sprite.Group()

brick_sprites = {
	'blue': [
		os.path.join(BASE_DIR, 'assets/blocks/01-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/02-Breakout-Tiles.png'),
	],
	'green': [
		os.path.join(BASE_DIR, 'assets/blocks/03-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/04-Breakout-Tiles.png'),
	],
	'violet': [
		os.path.join(BASE_DIR, 'assets/blocks/05-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/06-Breakout-Tiles.png'),
	],
	'red': [
		os.path.join(BASE_DIR, 'assets/blocks/07-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/08-Breakout-Tiles.png'),
	],
	'orange': [
		os.path.join(BASE_DIR, 'assets/blocks/09-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/10-Breakout-Tiles.png'),
	],
	'light_blue': [
		os.path.join(BASE_DIR, 'assets/blocks/11-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/12-Breakout-Tiles.png'),
	],
	'yellow': [
		os.path.join(BASE_DIR, 'assets/blocks/13-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/14-Breakout-Tiles.png'),
	],
	'dark_green': [
		os.path.join(BASE_DIR, 'assets/blocks/15-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/16-Breakout-Tiles.png'),
	],
	'gray': [
		os.path.join(BASE_DIR, 'assets/blocks/17-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/18-Breakout-Tiles.png'),
	],
	'brown': [
		os.path.join(BASE_DIR, 'assets/blocks/19-Breakout-Tiles.png'),
		os.path.join(BASE_DIR, 'assets/blocks/20-Breakout-Tiles.png'),
	],
}

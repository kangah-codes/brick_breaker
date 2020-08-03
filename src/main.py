from game.player import *
from game.brick import *



level = 1
p = Player()

def game():
	# b = Brick(100, 100)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	running = True

	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill((0,0,0))

		if len(brick_group) == 0:
			for i in range(SCREEN_WIDTH):
				for y in range(level):
					if i % 80 == 0 and y % 40 == 0:
						brick_group.add(Brick(i, y))

		p.update()
		p.draw(screen)

		brick_group.update()
		brick_group.draw(screen)
		pygame.display.update()

game()
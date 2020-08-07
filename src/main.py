from game.player import *
from game.brick import *
from game.general_sprites import *



level = 4

b = Ball(100, 100)

# always create player after ball
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
			if event.type == pygame.KEYDOWN:
				global level
				if event.key == pygame.K_SPACE:
					level += 1
					brick_group.empty()
				elif event.key == pygame.K_b:
					level -= 1
					brick_group.empty()

		screen.fill((0,0,0))

		if len(brick_group) == 0:
			for i in range(SCREEN_WIDTH):
				for y in range(level*BRICK_HEIGHT):
					if i % 80 == 0 and y % 40 == 0:
						brick_group.add(Brick(i, y))


		brick_group.update()
		brick_group.draw(screen)

		p.update()
		p.draw(screen)

		b.update(p)
		b.draw(screen)

		pygame.display.update()

game()
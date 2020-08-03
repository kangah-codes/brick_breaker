from config.settings import *
from .animate import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		# player attributes
		self.state = 'healthy'
		
		self.image = Animation(player_sprites.get(self.state), 0.25)
		self.speed = 1
		self.pos = pygame.math.Vector2()
		self.pos.x = 100
		self.pos.y = 100
		self.rect = self.image.get_rect()

	def update_state(self, state):
		self.state = state
		# only creating an animated sprite if we have 2 or more sprites in the state
		self.image = Animation(player_sprites.get(self.state), SCALE) if len(player_sprites.get(self.state)) > 1 else player_sprites.get(self.state)[0]
		# setting player speeds based on player state
		self.speed = 1 if self.state == 'healthy' else 0.5 if self.state == 'slow' else 2 if self.state == 'fast' else 1

	def update(self):
		# updating our player only if it is an animation
		if type(self.image) == Animation:
			self.image.animate(DT)
			self.rect = self.image.get_current_image().get_rect()
		self.rect = self.image.get_rect()
		# movement for player
		keyPress = pygame.key.get_pressed()

		if keyPress[pygame.K_a]:
			self.pos.x -= self.speed
		elif keyPress[pygame.K_d]:
			self.pos.x += self.speed

		self.rect.x, self.rect.y = self.pos.x, self.pos.y

		# making infinite screen
		if self.pos.x + self.rect.width < 0:
			self.pos.x = SCREEN_WIDTH
		elif self.pos.x > SCREEN_WIDTH:
			self.pos.x = 0 - self.rect.width

	def draw(self, display):
		if type(self.image) == Animation:
			drawImage = self.image.get_current_image()
		else:
			drawImage = self.image
		display.blit(drawImage, (self.pos.x, self.pos.y))


p = Player()


def game():
	clock.tick(FPS)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					states = ['healthy', 'shrunk', 'fast', 'slow']
					p.update_state(random.choice(states))
					
		screen.fill((0,0,0))

		p.update()
		p.draw(screen)

		pygame.display.update()
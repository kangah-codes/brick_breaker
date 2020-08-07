from config.settings import *
from config.player_settings import *
from .animate import *
from .general_sprites import ball_group

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		# player attributes
		self.state = 'healthy'
		
		self.image = Animation(player_sprites.get(self.state), SCALE)
		self.speed = NORMAL_SPEED
		self.pos = pygame.math.Vector2()
		self.pos.x = 100
		self.pos.y = Y_LOCATION
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.get_image())

	def update_state(self, state):
		self.state = state
		# only creating an animated sprite if we have 2 or more sprites in the state
		self.image = Animation(player_sprites.get(self.state), SCALE) if len(player_sprites.get(self.state)) > 1 else player_sprites.get(self.state)[0]
		# setting player speeds based on player state
		self.speed = NORMAL_SPEED if self.state == 'healthy' else SLOW_SPEED if self.state == 'slow' else FAST_SPEED if self.state == 'fast' else NORMAL_SPEED

	def update(self):
		# updating player mask
		self.mask = pygame.mask.from_surface(self.get_image())
		# updating our player only if it is an animation
		if type(self.image) == Animation:
			self.image.animate(DT)
		self.rect = self.get_image().get_rect()

		# movement for player
		keyPress = pygame.key.get_pressed()

		if keyPress[pygame.K_a]:
			self.pos.x -= self.speed
		elif keyPress[pygame.K_d]:
			self.pos.x += self.speed

		# setting our x rect and y rect positions to player position
		self.rect.x, self.rect.y = self.pos.x, self.pos.y

		# making infinite screen
		if self.pos.x + self.rect.width < 0:
			self.pos.x = SCREEN_WIDTH
		elif self.pos.x > SCREEN_WIDTH:
			self.pos.x = 0 - self.rect.width

	def get_image(self):
		# returning current image if current player state is an animation
		# else return the normal pygame surface

		if type(self.image) == Animation:
			return self.image.get_current_image()
		return self.image

	def draw(self, display):
		if type(self.image) == Animation:
			drawImage = self.image.get_current_image()
		else:
			drawImage = self.image

		# draw points around player mask
		# [pygame.draw.circle(display, (255,255,255), [x[0], x[1]], 1, 1) for x in self.mask.outline()]
		display.blit(drawImage, (self.pos.x, self.pos.y))

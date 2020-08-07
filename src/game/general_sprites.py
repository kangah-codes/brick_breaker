from config.settings import *

# global ball settings
easy = True if DIFFICULTY == 1 or DIFFICULTY == 2 else False

ball_group = pygame.sprite.Group()

class Ball(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets/ball.png")), (25, 25))
		self.pos = pygame.math.Vector2()
		self.pos.x, self.pos.y = x, y
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.collision_switch = False
		if easy:
			self.y_speed, self.x_speed = BALL_SPEED, BALL_SPEED
		else:
			self.y_speed, self.x_speed = BALL_SPEED * 1.5, BALL_SPEED * 1.5

	def update(self, player):
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.x, self.rect.y = self.pos.x, self.pos.y

		self.pos.y += self.y_speed
		self.pos.x += self.x_speed

		# if ball hits either side of screen (top/bottom)
		if (self.pos.y + self.rect.height) > SCREEN_HEIGHT or self.pos.y < 0:
			self.flipY()

		# if ball hits right/left side of screen
		if self.pos.x < 0 or (self.pos.x + self.rect.width) > SCREEN_WIDTH:
			self.flipX()

		# check for collision with player
		if pygame.sprite.collide_mask(self, player):
			# self.flipX()
			# self.flipY()


	def flipY(self):
		self.y_speed *= -1

	def flipX(self):
		self.x_speed *= -1


	def draw(self, display):
		# print(player.get_image())
		# print(current_player_mask)
		display.blit(self.image, (self.pos.x, self.pos.y))


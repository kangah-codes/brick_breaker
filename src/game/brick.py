from config.settings import *
from config.brick_settings import *

class Brick(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		# simplifying this operation so we dont have to use the or operator when checking game difficulty
		self.easy = True if DIFFICULTY == 1 or DIFFICULTY == 2 else False
		# variable for holding which key in the dictionary our type of brick is
		self.sprite_key = random.choice(list(brick_sprites.keys()))
		self.image = pygame.transform.scale(pygame.image.load(brick_sprites.get(self.sprite_key)[0]), (BRICK_WIDTH, BRICK_HEIGHT))
		self.rect = self.image.get_rect()
		if self.easy:
			# easy mode			
			self.life = 1
		else:
			# loading damaged image srpites based on game difficulty
			self.damaged_image = pygame.transform.scale(pygame.image.load(brick_sprites.get(self.sprite_key)[-1]), (BRICK_WIDTH, BRICK_HEIGHT))
			self.life = 2

		self.pos = pygame.math.Vector2()
		self.pos.x, self.pos.y = x, y


	def update(self):
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.pos.x, self.pos.y

		# destroying bricks when their life is zero
		if self.life <= 0:
			self.kill()


	def draw(self, display):
		if not self.easy and self.life <= 1:
			display.blit(self.damaged_image, (self.pos.x, self.pos.y))
		else:
			display.blit(self.image, (self.pos.x, self.pos.y))


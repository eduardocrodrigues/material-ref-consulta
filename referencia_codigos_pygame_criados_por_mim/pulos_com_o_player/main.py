import pygame

vec = pygame.math.Vector2

# colors 

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = 600
HEIGHT = 500

FPS = 60


class Player(pygame.sprite.Sprite):

	def __init__(self, w, h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((w, h))
		self.image.fill(YELLOW)
		self.rect = self.image.get_rect()
		self.speed = vec(0, 0)
		self.vel = 0 #vec(0, 0)
		self.gravity = 1 #vec(0, 5)
		self.forca_do_pulo = 15 #vec(0, -5)
		self.jumping = False
		self.quant_pulos = 0 # faz o incremento da quantidade de pulos que o player
		self.quant_pulos_player = 4 # define o limite da quantidade de pulos que o player pode dar


	def update(self):

		self.vel += self.gravity
		self.rect.y += self.vel # atribui a gravidade no eixo y do retângulo do player

		self.speed = vec(0, 0) # zera o eixo x,y da velocidade do player quando soltamos o botao do teclado

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.speed.x = -5
		if keys[pygame.K_d]:
			self.speed.x = 5


		self.rect.x += self.speed.x # atribui a velocidade no eixo x do retângulo do player

		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT



	def jump(self):

		# se o player relar no chao da tela, a quantidades de pulos dadas pelo player zera novamente
		if self.rect.bottom == HEIGHT:
			self.quant_pulos = 0

		if self.quant_pulos < self.quant_pulos_player: # o valor de self.quant_pulos_player é: 2
			self.quant_pulos += 1 # conta quantos pulos o player deu...
			self.jumping = True
			if self.jumping == True:
				self.vel = -self.forca_do_pulo # inverte o valor da velocidade da gravidade













		


		




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player1 = Player(32, 32)
all_sprites.add(player1)

running = True

while running:

	screen.fill(GREEN)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player1.jump()



	all_sprites.update()

	# draw
	all_sprites.draw(screen)



	pygame.display.update()
	clock.tick(FPS)






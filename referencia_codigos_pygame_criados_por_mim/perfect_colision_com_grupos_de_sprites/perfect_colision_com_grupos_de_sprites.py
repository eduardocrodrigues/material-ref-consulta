import pygame

##############################################
# faz o carregamento das imagens para usarmos no jogo
#
img_p = pygame.image.load('playerShip1_orange.png')
img_player = pygame.transform.scale(img_p, (50, 40))

img_e = pygame.image.load('enemyBlue1.png')
img_enemy = pygame.transform.scale(img_e, (50, 40))

img_p2 = pygame.image.load('playerShip1_green.png')
img_player2 = pygame.transform.scale(img_p2, (50, 40))

#########################################
# CONSTANTES
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 30


######################################
# a classe criada para o nosso player
#
class Player(pygame.sprite.Sprite):

#
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = img_player
		self.player_mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.speed = pygame.math.Vector2(5, 5)



	def update(self):
		self.control()

	def control(self):

		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.rect.centerx += self.speed[0]
		if keys[pygame.K_a]:
			self.rect.centerx -= self.speed[0] 
		if keys[pygame.K_w]:
			self.rect.centery -= self.speed[1]
		if keys[pygame.K_s]:
			self.rect.centery += self.speed[1] 


####################################################
# a classe criada para o nosso inimigo
#
class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = img_enemy
		self.enemy_mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		# self.posX = 600
		# self.posY = 200
		self.rect.centerx = 600 / 2
		self.rect.centery = 200 / 2
		self.speed = pygame.math.Vector2(0, 0)


	# def update(self):

	# 	# self.rect.centerx -= 5
	# 	pass		



##########################################################
# inicia a estrutura básico de um jogo (o core do jogo) 
#
pygame.init()
screen = pygame.display.set_mode((600, 400)) # define o tamanho da tela do jogo
clock = pygame.time.Clock() # inserimos a classe Clock na variável clock


all_sprites = pygame.sprite.Group() # cria o grupo que armazena o todas as sprites do jogo
player1 = Player()
all_sprites.add(player1)

enemy_group1 = pygame.sprite.Group() # cria o grupo que armazena o inimigo do jogo
enemy1 = Enemy() # criado o inimigo
enemy_group1.add(enemy1) # adicionamos o inimigo ao grupo dele
all_sprites.add(enemy_group1) # adicionamos o inimigo criado ao grupo que contêm todas as sprites do jogo


running = True # variável do loop principal do jogo

##############################################
# loop principal do jogo
#
while running:

	screen.fill(BLACK) # limpa os rastros de todos os objetos desenhados (rastro das sprites desenhadas) na tela do jogo.

	#########################################################
	# checa se clicamos no botão de sair da janela do jogo
	#
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	##################################################
	# bloco de código que faz a checagem da colisão do player com o inimigo
	# usando maskara de colisão (tbm chamado de: Pixel Perfect)
	#
	hit = pygame.sprite.spritecollide(player1, enemy_group1, False, pygame.sprite.collide_mask)
	if hit: # se a colisão for True
		player1.image = img_player2 # trocamos a imagem da nave vermelha do player pela nave verde 
		# print('colidiu !!!!')
	else:
		player1.image = img_player # se não houver colisão, a imagem da nave verde é trocada pela imagem da nave vermelha


	pygame.draw.rect(screen, (255, 0, 0), player1.rect, 4) # desenha a borda vermelha em volta do nosso player
	all_sprites.draw(screen) # desenha todas as sprites do jogo na tela
	all_sprites.update() # chama o método update() de todos os objetos do grupo all_sprites

	pygame.display.update() # atualiza a tela do jogo
	clock.tick(FPS) # atualiza a tela do jogo a cada 30 segundos
	# print('tick', clock.tick(FPS))



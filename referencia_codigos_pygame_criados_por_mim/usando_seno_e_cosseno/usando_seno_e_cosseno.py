import pygame
import math

###########################################
# CONSTANTES DA TELA DO PYGAME 
#
WIDTH = 500
HEIGHT = 400
HW = int(WIDTH / 2)
HH = int(HEIGHT / 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # define a tela do pygame
clock = pygame.time.Clock() # classe time do pygame para controle de frames do jogo
############################################
# Cria o bloco que gira na tela
# 
surf = pygame.Surface((30, 30)) # cria o bloco do jogo
surf.fill((255, 0, 0)) # define a cor do bloco
p_rect = surf.get_rect() # gera uma área retângular para a surface 
p_rect.center = (WIDTH/2, HEIGHT/2) # insere o quadrado no centro da tela
#########################################################
# variáveis que são usadas nos métodos seno e cosseno
# 
# definimos o angulo que será usado em cosseno (eixo x) e seno (eixo y).
#	OBS: o angulo DEVE SER SEMPRE USADO como unidade de medida EM RADIANOS
#
angle = math.radians(25) # valor em radianos
velocity = 4 # define a velocidade em que o quadrado vermelho vai percorrer de acordo com os angulos de seno e cosseno 
cos = 0 # definindo a variável que recebe o valor do metodo math.cos()
sin = 0 # definindo a variável que recebe o valor do metodo math.sin()


running = True # loop do jogo

while running:
	screen.fill((0, 0, 0)) # limpa os rastros do(s) objeto(s) na tela

	# checa por eventos na janela do pygame
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()


	########################################################################
	# aqui é onde inserimos o centro do quadrado vermelho no centro da tela
	#
	p_rect.center = (HW+(p_rect.width/2),HH+(p_rect.height/2))

	################################################################
	# aqui inserimos um valor de ângulo para seno (math.sin(angle)) 
	#	OBS: seno representa o eixo y da tela do pygame
	#
	sin -= math.sin(angle) * velocity
	# aqui inserimos um valor de ângulo para coseno (math.cos(angle)) 
	#	OBS: cosseno representa o eixo x da tela do pygame
	#
	cos += math.cos(angle) * velocity

	######################################################################################
	# Desenhamos o quadrado vermelho, a bolinha amarela e a linha verde na tela do pygame
	#
	# desenha o quadrado 35 pixels a mais do centro da tela em x
	screen.blit(surf, (p_rect.x+cos, p_rect.y+p_rect.height/2+sin)) 
	pygame.draw.circle(screen, (255, 255, 0), (HW, HH), 5) # desenha a bolinha amarela no centro do quadrado vermelho
	# desenha a linha verde, uma ponta da linha fica no centro do quadrado, a outra ponta fica no centro da tela do pygame
	pygame.draw.line(screen, (0, 200, 0), (p_rect.centerx+cos, p_rect.centery+sin+p_rect.width/2), (HW, HH), 2)

	angle += 0.1 # incrementa 0.1 a cada loop no angulo dos eixos de seno (eixo y) e cosseno (eixo x)


	pygame.display.update() # atualiza a tela do jogo
	clock.tick(30) # define os frames do jogo

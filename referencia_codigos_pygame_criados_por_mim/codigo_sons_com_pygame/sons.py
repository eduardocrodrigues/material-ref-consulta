import pygame
import os

WIDTH = 300
HEIGHT = 400

FPS = 60

RED = (170, 0, 0)
GREEN = (0, 170, 0)
BLUE = (0, 0, 170)
YELLOW = ( 200, 200, 0)

class Game:

	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()

		################################################################
		# juntamos o caminho do sistema operacional até a pasta sound...
		sounds_path = os.path.join(os.path.dirname(__file__), 'sound')

		#######################################################
		# definimos o caminho da pasta sound junto com 
		# os nomes dos arquivos de cada som...
		sound1 = os.path.join(sounds_path, 'expl3.wav')
		sound2 = os.path.join(sounds_path, 'pew.wav')
		sound3 = os.path.join(sounds_path, 'expl6.wav')
		sound4 = os.path.join(sounds_path, 'pew2.wav')


		################################################
		# inicia o módulo de sons e musica do pygame
		pygame.mixer.init()

		###############################################################################
		# define a quantidade de canais do nosso mixer (será USADO PAR OS SONS do jogo)
		#
		#  OBS: para vc entender melhor, quando utilizamos 
		#  o método: pygame.mixer.set_num_channels(numero), internamente o pygame CRIA 
		#  UM MIXER (igual a um mixer de produção musical), com vários canais, onde cada
		#  canal podemos inserir um tipo do som diferente. A quantidade de canais padrão
		#  de um mixer é: 8
		#
		#  OBS2: lembre-se que, som é diferente de música. Som SÃO OS BARULHOS que acontecem
		#  DURANTE O JOGO, como por exemplo: um som de explosão, um som de tiro, um som executado  
		#  quando pegamos um powerup, etc... 
		#  
		#  MÚSICA, por exemplo, é a musica que toca durante o jogo.
		# 
		#  como mostra a linha abaixo, criamos um mixer com somente 8 canais (é a quantidade padrão)...
		pygame.mixer.set_num_channels(8) # padrão

		#####################################
		# define os canais que queremos reservar no mixer do pygame para inserir os sons do jogo...
		#
		#  OBS: os NÚMERO ARMAZENADO NOS PARÊNTESES do método: pygame.mixer.set_reserved(num),
		#  representam A NÚMERAÇÃO DE UM CANAL do mixer criado com o método: pygame.mixer.set_num_channels(num)
		#
		#  minha_dúvida: sinseramente eu não sei como funcionaria o código se reservassemos 
		#  aguns canais do mixer e para usar e outros não. Na dúvida, eu crio os canais que eu preciso, 
		#  reservo todos eles, e utilizo cada um deles para cada um dos sons que eu preciso, exatamente 
		#  como fizemos nesse código.
		pygame.mixer.set_reserved(0)
		pygame.mixer.set_reserved(1)
		pygame.mixer.set_reserved(2)


		###############################################################
		# inserimos cada som dentro de uma classe: pygame.mixer.Sound(),
		# para podermos inserir dentro dos canais do mixer 
		# do pygame, ou seja, para podermos inserir os sons dentro dos
		# parênteses da classe: pygame.mixer.Channel()
		self.firstSound = pygame.mixer.Sound(sound1)
		self.secondSound = pygame.mixer.Sound(sound2)
		self.thirdSound = pygame.mixer.Sound(sound3)
		self.fourthSound = pygame.mixer.Sound(sound4)


		self.running = True



		self.loop()

	def loop(self):

		while self.running:

			#self.screen.fill(RED)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						self.screen.fill(RED)
						###############################
						# pega o canal zero do mixer do pygame e 
						# toca no método play() do canal o som self.firstSound
						pygame.mixer.Channel(0).play(self.firstSound)
					if event.key == pygame.K_d:
						self.screen.fill(GREEN)						
						###############################
						# pega o canal um do mixer do pygame e 
						# toca no método play() do canal o som self.secondSound
						pygame.mixer.Channel(1).play(self.secondSound)
					if event.key == pygame.K_w:
						self.screen.fill(BLUE)
						###############################
						# pega o canal dois do mixer do pygame e 
						# toca no método play() do canal o som self.thrirdSound
						pygame.mixer.Channel(2).play(self.thirdSound)
					if event.key == pygame.K_s:
						self.screen.fill(YELLOW)
						###############################
						# pega o canal três do mixer do pygame e 
						# toca no método play() do canal o som self.fourthSound
						pygame.mixer.Channel(3).play(self.fourthSound)
						



			pygame.display.update()
			self.clock.tick(FPS)


if __name__ == '__main__':
	Game()


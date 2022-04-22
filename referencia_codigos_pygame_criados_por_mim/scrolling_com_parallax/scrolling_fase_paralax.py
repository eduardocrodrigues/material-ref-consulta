import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIGHTBLUE = (184,245,237)


WIDTH = 900
HEIGHT = 500

pygame.init()
pygame.display.set_caption('teste')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

#player = pygame.Surface((30,30))
#player.fill(RED)
player = pygame.image.load('img/sprite.png')
player_rect = player.get_rect()
player_rect.x = 35
player_rect.y = 258

vel_x = 0
vel_y = 0
gravidade = 0.60
forca_do_pulo = 12
quant_pulos = 0
max_pulos = 1


img_grama = pygame.image.load('img/tile_grama.png')

img_terra = pygame.image.load('img/tile_terra.png')

# faz a fase rolar para a direita e esquerda
true_scroll = [0, 0]

# são as dimensões dos quadrados do fundo da fase que serão
# usados para o efeito parallax.
# As representações do valores na lista sao:
# 0.25 e 0.05 -> são os MULTIPLICADORES da área retangular que
# será desenhado no fundo da fase. São esses números que faz o
# efeito de movimentação das áreas retangulares desenhadas no
# fundo da tela quando movimentamos o jogador na fase.
# [120, 10, 70, 600] -> é uma das 5 áreas retangulares que serão
# desenhadas no fundo da fase.
background_objects = [[0.25,[120,10,70,600]],
                      [0.25,[280,30,40,600]],
                      [0.5,[30,40,40,600]],
                      [0.5,[130,90,100,600]],
                      [0.5,[300,80,120,600]]]



game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','1','1','1','1','1','0','0','0','0','1','1','1','1','1','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1'],
            ['2','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','2'],
            ['2','2','2','2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2'],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2']]

def colide_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


while True:
   

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_x += 5
            if event.key == pygame.K_LEFT:
                vel_x -= 5
            if event.key == pygame.K_UP:
                #vel_y = -forca_do_pulo
                if quant_pulos < max_pulos:
                    quant_pulos += 1
                    vel_y = -forca_do_pulo



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel_x = 0
            if event.key == pygame.K_LEFT:
                vel_x = 0
            if event.key == pygame.K_UP:
                vel_y = 0


    # limpa o rastro dos objetos que movimentam na tela
    screen.fill(LIGHTBLUE)

    # variáveis somente para armazenar a metade da largura e altura da tela,
    # que serão inseridos no centro do player.
    metade_largura_tela = WIDTH/2
    metade_altura_tela = HEIGHT/2
    # na primeira passada do loop do jogo, o valor no eixo X da tela em 
    # scroll[x] recebe o valor de player.x. Quando movimentamos o player para 
    # a frente, FAZEMOS A SUBTRAÇÂO do valor de player.x (que foi atribuido
    # a scroll[x]) com o novo valor atual de player.x. É por isso que ao
    # movimentar o player para a frente, a fase inteira se move para trás e
    # vise-versa.
    # OBS: tem que inserir as variáveis true_scroll[x] e true_scroll[y] no
    # X e Y do blit() do loop que desenha os tiles na tela.
    # OBS2: fazer a divisão por 20 no true_scroll da tela deixa uma
    # movimentação mais suave na camera do jogo ao movimentar o player.
    true_scroll[0] += (player_rect.x-true_scroll[0]-metade_largura_tela-6)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-metade_altura_tela-16)/20
    # fizemos uma cópia do array true_scroll para a variavel scroll...
    scroll = true_scroll.copy()
    # reatribuimos numeros no formato inteiros no (X,Y) da camera pq
    # se vc deixar a rolagem da camera em números quebrados (diferentes de
    # numeros inteiros), haverá uma leve sobreposição de pixels na fase ao
    # movimentar o personagem para direita ou para a esquerda.
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])


    # Aqui é desenhado o fundo retangular grande de cor verde escuro que
    # preenche a metade da tela.
    pygame.draw.rect(screen, (7, 80, 75), pygame.Rect(0, 300, 900, 600))
    
    for background_object in background_objects:
        # background_object representa cada lista no array background_objects. 
        # Background_object[1][0] é o valor 125 da lista interna em background_object,
        # scroll[0] é a posição X da camera,
        # background_object[0] é o valor 0.25 (valor multiplicador do eixo (X,Y) de
        # movimentação das áreas retangulares desenhados no fundo da fase) na
        # lista background_object.
        # OBS: se vc quiser deixar o efeito parallax no fundo da fase SEM A MOViMENTAÇÃO
        # NO EIXO X (sem que as áreas retangulares se movam no eixo X), é só
        # retirar o trecho (-scroll[0]*background_object[0]) do eixo X, na criação do retângulo.
        obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],
                               background_object[1][1]-scroll[1]*background_object[0],
                               background_object[1][2],
                               background_object[1][3])


        # quando a lista background_object tiver o multiplicador 0.5...
        if background_object[0] == 0.5:
            # é desenhado na tela a área retangular de cor verde (mais clara)
            # OBS: O efeito parallax acontece pq as áreas retângulares definidas DENTRO DA
            # LISTA CRIADA INTERNAMENTE EM background_object são multiplicadas pelo valor 0.5 definido
            # na lista background_object.
            pygame.draw.rect(screen,(14,222,150),obj_rect)
        else:
            # é desenhado na tela a área retangular de cor verde (mais escura)
            # OBS: O efeito parallax acontece pq as áreas retângulares definidas DENTRO DA
            # LISTA CRIADA INTERNAMENTE EM background_object são multiplicadas pelo valor 0.25 definido
            # na lista background_object.
            pygame.draw.rect(screen,(9,91,85),obj_rect)


    tiles_rect = []

    y = 0
    for lista in game_map:
        x = 0
        for num in lista:
            if num == '1':
                screen.blit(img_grama,(x*32-scroll[0], y*32-scroll[1]))
            if num == '2':
                screen.blit(img_terra,(x*32-scroll[0], y*32-scroll[1]))
            if num != '0':
                # pega a area retangular de cada tile na mesma posição em que estão inseridos na tela do jogo.
                tiles_rect.append(pygame.Rect(x*32, y*32, 32, 32))
            x += 1
        y += 1


    screen.blit(player, (player_rect.x-scroll[0], player_rect.y-scroll[1]))

    #print(player_rect.x)
    #print()
    #print(player_rect.y)


    # a gravidade do player é adicionada na velocidade, no eixo y do player
    vel_y += gravidade
    # assim que a velocidade y do player é incrementada...
    player_rect.y += vel_y
    # é feita a checagem de colisão do player com as áreas retangulares
    # inseridas no array tiles_rect, se houver colisão, a função colide_test()
    # retorna um array com todas as áreas retangulares em que o player colidiu.
    hit_list = colide_test(player_rect, tiles_rect)
    # se houver colisão em hit_list, é feita a verificação do bottom do player e
    # do topo do player... 
    for block in hit_list:
        # se ao colidir, a velocidade do eixo y for MAIOR que zero...
        if vel_y > 0:
            # o bottom do player recebe o topo da área retangular que foi colidida.
            player_rect.bottom = block.top
            # retira a incrementação da gravidade 
            vel_y = 0
            # zera a quantidade de pulos do player
            quant_pulos = 0
        # se ao colidir, a velocidade do eixo y for MENOR que zero...
        if vel_y < 0:
            # o topo do player recebe o bottom da área retangular que foi colidida.
            player_rect.top = block.bottom

    
    player_rect.x += vel_x

    hit_list = colide_test(player_rect, tiles_rect)

    for block in hit_list:
        if vel_x > 0:
            player_rect.right = block.left
        if vel_x < 0:
            player_rect.left = block.right


    # 
    if player_rect.y + player_rect.height >= HEIGHT:
        player_rect.y = HEIGHT - player_rect.height
        vel_y = 0



    clock.tick(60)
    pygame.display.update()

    

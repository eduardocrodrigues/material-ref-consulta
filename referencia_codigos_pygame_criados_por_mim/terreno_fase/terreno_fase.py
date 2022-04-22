import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


WIDTH = 900
HEIGHT = 500

pygame.init()
pygame.display.set_caption('teste')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

player = pygame.Surface((30,30))
player.fill(RED)
player_rect = player.get_rect()
player_rect.x = 35
player_rect.y = 258

vel_x = 0
vel_y = 0
gravidade = 0.60
forca_do_pulo = 12
quant_pulos = 0
max_pulos = 1


plataforma = pygame.Surface((60, 20))
plataforma.fill(WHITE)
plataforma_rect = plataforma.get_rect()
plataforma_rect.x = 50
plataforma_rect.y = 80


img_grama = pygame.image.load('img/tile_grama.png')

img_terra = pygame.image.load('img/tile_terra.png')




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
    screen.fill(BLACK)


    tiles_rect = []

    y = 0
    for lista in game_map:
        x = 0
        for num in lista:
            if num == '1':
                screen.blit(img_grama,(x*32, y*32))
            if num == '2':
                screen.blit(img_terra,(x*32, y*32))
            if num != '0':
                # pega a area retangular de cada tile na mesma posição em que estão inseridos na tela do jogo.
                tiles_rect.append(pygame.Rect(x*32, y*32, 32, 32))
            x += 1
        y += 1


    screen.blit(player, (player_rect.x, player_rect.y))

    print(player_rect.x)
    print()
    print(player_rect.y)


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

    

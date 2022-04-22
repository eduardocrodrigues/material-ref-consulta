import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)


WIDTH = 600
HEIGHT = 500

pygame.init()
pygame.display.set_caption('teste')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

#jogador1
player_rect = pygame.Surface((30,30))
player_rect.fill(RED)
player = player_rect.get_rect()

vel_x = 0
vel_y = 0
gravidade = 0.60
forca_do_pulo = 17


#plataforma1
surf = pygame.Surface((90, 20))
surf.fill(WHITE)
plataforma = surf.get_rect()
plataforma.x = 50
plataforma.y = 440


#plataforma2
surf2 = pygame.Surface((120, 60))
surf2.fill(WHITE)
plataforma2 = surf2.get_rect()
plataforma2.x = 250
plataforma2.y = 340


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
                # aplica a força do pulo no player
                vel_y = -forca_do_pulo                
            if event.key == pygame.K_DOWN:  
                vel_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel_x = 0
            if event.key == pygame.K_LEFT:
                vel_x = 0
            if event.key == pygame.K_UP:
                vel_y = 0
            if event.key == pygame.K_DOWN:
                vel_y = 0



    screen.fill(BLACK)

    #player
    screen.blit(player_rect, (player.x, player.y))

    # plataforma1 para pular
    screen.blit(surf, (plataforma.x, plataforma.y))

    # plataforma2 para pular
    screen.blit(surf2, (plataforma2.x, plataforma2.y))

    # armazena a area retângular da plataforma
    platform_rects = []
    platform_rects.append(plataforma)
    platform_rects.append(plataforma2)


    # atribui a velocidade ao x do player
    player.x += vel_x

    # retorna os blocos que houve colisão com o player
    hit_block_list = colide_test(player, platform_rects)
     
    for block in hit_block_list:
        if vel_x > 0:
            player.right = block.left
        elif vel_x < 0:
            player.left = block.right

    # atribui a gravidade ao y do retângulo do player
    vel_y += gravidade
    # adiciona a velocidade ao y do player
    player.y += vel_y 

    # retorna os blocos que houve colisão com o player
    hit_block_list = colide_test(player, platform_rects)

    for block in hit_block_list:
        if vel_y > 0:
            player.bottom = block.top
            vel_y = 0
        if vel_y < 0:
            player.top = block.bottom
            


    # não deixa o player passar do tamanho da tela
    if player.y + player.height >= HEIGHT:
        player.y = HEIGHT - player.height
        vel_y = 0


    clock.tick(60)
    pygame.display.update()


"""
hit_list = colide_test(player, platform_rects)

    for tile in hit_list:
        if player.bottom > tile.top: 
            player.bottom = tile.top
            vel_y = 0

        if player.top < tile.bottom:
            player.top = tile.bottom
            vel_y = 0
            #print('colidiu')


    vel_y += gravidade
    player.y += vel_y

    hit_list = colide_test(player, platform_rects)
    for tile in hit_list:
        if player.right > 0:
            player.right = tile.left
            vel_x = 0
"""

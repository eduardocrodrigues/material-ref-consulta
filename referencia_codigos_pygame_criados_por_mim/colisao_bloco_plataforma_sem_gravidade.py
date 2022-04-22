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
gravidade = 1
forca_do_pulo = 25


#plataforma
surf = pygame.Surface((90, 20))
surf.fill(WHITE)
plataforma = surf.get_rect()
plataforma.x = 50
plataforma.y = 440


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
                #vel_y += -forca_do_pulo
                vel_y -= 5                
            if event.key == pygame.K_DOWN:
                #vel_y = -forca_do_pulo
                vel_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel_x = 0
            if event.key == pygame.K_LEFT:
                vel_x = 0
            if event.key == pygame.K_UP:
                #vel_y = -forca_do_pulo
                vel_y = 0
            if event.key == pygame.K_DOWN:
                #vel_y = -forca_do_pulo
                vel_y = 0



    screen.fill(BLACK)

    #player
    screen.blit(player_rect, (player.x, player.y))

    # plataforma para pular
    screen.blit(surf, (plataforma.x, plataforma.y))

    # armazena a area retângular da plataforma
    platform_rects = []
    platform_rects.append(plataforma)


    # atribui a velocidade ao x do player
    player.x += vel_x

    # retorna os blocos que houve colisão com o player
    hit_block_list = colide_test(player, platform_rects)
     
    for block in hit_block_list:
        if vel_x > 0:
            player.right = block.left
        elif vel_x < 0:
            player.left = block.right


    player.y += vel_y

    # retorna os blocos que houve colisão com o player
    hit_block_list = colide_test(player, platform_rects)

    for block in hit_block_list:
        if vel_y > 0:
            player.bottom = block.top
        if vel_y < 0:
            player.top = block.bottom
        


    # atribui a gravidade ao y do retângulo do player
    #vel_y += gravidade
    #player.y += vel_y

    


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

import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 30

the_obstacle = pygame.image.load('obstacle-400x399.png').convert_alpha() # carrega a imagem que é o nosso obstaculo
#obstacle = pygame.transform.scale(the_obstacle,(200, 200)) # redimensiona a imagem do nosso obstáculo
obstacle_mask = pygame.mask.from_surface(the_obstacle) # cria a maskara da imagem (onde tem cor na imagem representa a PRESENÇA DE BITES (numero 1) e onde não tem cor representa a AUSÊNCIA DE BITES (numero 0))
obstacle_rect = the_obstacle.get_rect() # cria a áre retângular para testarmos a colisão
center_x_obstacle = int(WIDTH / 2) - obstacle_rect.center[0] # guarda o valor do centro da tela subtraindo o valor do eixo x do centro do the_obstacle.
center_y_obstacle = int(HEIGHT / 2) - obstacle_rect.center[1] # guarda o valor do centro da tela subtraindo o valor do eixo y do centro do the_obstacle




green_blob = pygame.image.load('greenblob-59x51.png').convert_alpha() # carrega a imagem verde
orange_blob = pygame.image.load('orangeblob-59x51.png').convert_alpha() # carrega a imagem laranja
blob_mask = pygame.mask.from_surface(green_blob) # cria a maskara para a imagem, preparando a imagem para fazer o perfect collision (onde tiver cor na imagem representa a PRESENÇA DE BITES (numero 1) e onde não tem cor representa a AUSÊNCIA DE BITES (numero 0))
blob_rect = green_blob.get_rect() #
blob_color = green_blob #

running = True
while running:

    screen.fill(BLACK)

    mouse_x, mouse_y = pygame.mouse.get_pos() # pega a posição do mouse na tella

    offset = (mouse_x - center_x_obstacle, mouse_y - center_y_obstacle) # 

    result = obstacle_mask.overlap(blob_mask, offset) # verifica se as coordenadas de offset sobrepõe a maskara blob_mask do green_blob.  

    if result:
        blob_color = orange_blob
    else:
        blob_color = green_blob


    screen.blit(the_obstacle, (center_x_obstacle, center_y_obstacle))
    screen.blit(blob_color, (mouse_x, mouse_y))
    
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    pygame.display.update()
    clock.tick(FPS)

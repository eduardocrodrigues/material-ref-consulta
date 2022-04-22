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

img1 = pygame.Surface((30, 40))
img1.fill(GREEN)
img1_rect = img1.get_rect()
vel_x = 0
vel_y = 0


img2 = pygame.Surface((100, 100))
img2.fill(RED)
img2_rect = img2.get_rect()


while True:

    screen.fill(BLACK)

    screen.blit(img1, (img1_rect.x, img1_rect.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        vel_x = 5

    elif key[pygame.K_LEFT]:
        vel_x = -5

    elif key[pygame.K_UP]:
        vel_y = -5

    elif key[pygame.K_DOWN]:
        vel_y = 5

    else:
        vel_x = 0
        vel_y = 0

    
    img1_rect.x += vel_x
    img1_rect.y += vel_y

    print('img1_rect.x: ', img1_rect.x)
    print('img1_rect.y: ', img1_rect.y)

    pygame.display.update()
    clock.tick(FPS)

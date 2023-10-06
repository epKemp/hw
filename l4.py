import pygame

WIDTH = 360
HEIGHT = 768
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()
bg = pygame.image.load("img/bg.png")
ground = pygame.image.load("img/ground.png")
bird_1 = pygame.image.load("img/bird1.png")
ground_x = 0

running = True
while running:
    "Игровой цикл"
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ground_x -= 1
    #print(ground_x)
    if ground_x <= -500:
        ground_x = 0

    screen.blit(bg, (0,0))
    screen.blit(ground, (ground_x,600))
    screen.blit(bird_1, (60, 284))
    pygame.display.flip()
pygame.quit()
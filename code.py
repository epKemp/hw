import random

import pygame

WIDTH = 360
HEIGHT = 700
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создаем экземпляр класса экран
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock() #  отсчеты времени (FPS)

bg = pygame.image.load("img/bg.png") # изображение фона
ground = pygame.image.load("img/ground.png") # изображение земли
ground_x = 0

score = 0
font = pygame.font.Font("game_font.ttf", 30)
text = font.render(f"Счёт: {score}", True, (255,228,196))
text_rect = text.get_rect()
text_rect.topleft = 0, 0

mouse_pos = pygame.mouse.get_pos()
mouse_keys = pygame.mouse.get_pressed()

def count_score():
    global score
    if not game_over:
        score += 0.1

restart_button = pygame.image.load("img/restart.png")
button_rect = restart_button.get_rect()
button_rect.center = WIDTH // 2, HEIGHT // 2

for a in range(120, 240):
    for b in range(330, 372):
        button_cords = (a, b)

def rs_button():
    global button_rect, game_over, restart_button
    if game_over == True :
        screen.blit(restart_button, button_rect)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, position: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y -75]
        if position == -1:
            self.rect.bottomleft = [x, y + 75]

    def update(self):
        self.rect.x -= 1



class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        self.velocity = 0.1
        for num in range(1, 4):
            img = pygame.image.load(f"img/bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        global game_over
        self.counter += 1
        self.bird_time = 5
        if self.counter > self.bird_time:
            self.counter = 0
            self.index += 1
            if self.index > 2:
                self.index = 0
        self.image = self.images[self.index]
        self.velocity += 0.2
        self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -3)
        self.rect.y += self.velocity
        # self.rect.y += 1
        if self.rect.y > 564:
            self.velocity = 0
            self.rect.y = 564
            game_over = True
        #if self.rect.top < 0:
          # self.velocity =  0
        if not game_over:
            # Обработка клика мыши
            if pygame.mouse.get_pressed()[0] == 1: # [0,0,0], нажали ЛКМ [1,0,0]
                if self.rect.top >= 50:
                    self.velocity = -3
            # Обработка нажатия на пробел
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if self.rect.top >= 50:
                    self.velocity = -3

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy1 = Bird(90, HEIGHT // 2)
bird_group.add(flappy1)
last_pipe = pygame.time.get_ticks()
pipe_freq = 5000 # частота появления труб

game_over = False
running = True
while running:
    'Игровой цикл'
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not game_over:
        ground_x = ground_x - 1
        if ground_x <= -500:
            ground_x = 0
    screen.blit(bg, (0, 0))  # отрисовка изображение

    time_now = pygame.time.get_ticks() # текущее время в игре
    if not game_over:
        if pipe_freq < time_now - last_pipe:
            pipe_height = random.randint(-100, 250) # задаем рандомную высоту трубы
            top_pipe = Pipe(WIDTH, HEIGHT // 2 + pipe_height +400, -1)
            bot_pipe = Pipe(WIDTH, HEIGHT // 2 + pipe_height -200, 1)
            last_pipe = time_now
            pipe_group.add(top_pipe, bot_pipe)

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, True):
        game_over = True

    if event.type == pygame.MOUSEMOTION:
        m_pos = event.pos
        print(m_pos)


    rs_button()

    if pygame.mouse.get_pressed()[0] == 1 and game_over == True:
        game_over = False
        score = 0

    pipe_group.draw(screen)
    pipe_group.update()

    bird_group.draw(screen)
    bird_group.update()

    text = font.render(f"Счёт: {int(score)}", True, (255,228,196))
    count_score()

    screen.blit(text, text_rect)
    screen.blit(ground, (ground_x, 600))
    pygame.display.flip() # обновление экрана

pygame.quit()

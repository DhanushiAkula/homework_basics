import pygame
pygame.init()
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mini Sprite Adventure")
BLUE = (0, 125, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x = 30
y = 30
sprite_width = 60
sprite_height = 60
speed = 3
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= speed
    if pressed[pygame.K_RIGHT]:
        x += speed
    if pressed[pygame.K_UP]:
        y -= speed
    if pressed[pygame.K_DOWN]:
        y += speed
        x = max(0, min(x, screen_width - sprite_width))
    y = max(0, min(y, screen_height - sprite_height))
    if x == 0:
        current_color = BLUE
    elif x == screen_width - sprite_width:
        current_color = YELLOW
    elif y == 0:
        current_color = RED
    elif y == screen_height - sprite_height:
        current_color = GREEN
    else:
        current_color = WHITE
    screen.fill(BLACK)
    pygame.draw.rect(
        screen,
        current_color,
        pygame.Rect(x, y, sprite_width, sprite_height)
    )
    pygame.draw.rect(
        screen,
        GREEN,
        pygame.Rect(150, 100, 60, 60),
        3
    )
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
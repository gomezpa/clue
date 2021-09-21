import pygame

# CONSTANT VARIABLES
background_color = (255, 255, 255)
(width, height) = (600, 400)
rectColor = (154, 194, 204)
rect = pygame.Rect(10, 10, 60, 60)

direction = {pygame.K_LEFT: (-10, 0),
             pygame.K_RIGHT: (10, 0),
             pygame.K_UP: (0, -10),
             pygame.K_DOWN: (0, 10)}
# PROPERTIES FOR THE SCREEN
screen = pygame.display.set_mode((width, height))
clueIcon = pygame.image.load('clue.ico')
pygame.display.set_icon(clueIcon)
pygame.display.set_caption('Clue')
screen.fill(background_color)

# BOOLEAN TO KEEP SCREEN UP UNTIL USER EXITS
running = True
release = False
pressed = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in direction:
                d = direction[event.key]
                rect.move_ip(d)
    screen.fill(background_color)
    pygame.draw.rect(screen, rectColor, rect)
    pygame.display.flip()



import pygame

pygame.init()
screen = pygame.display.set_mode((590, 500))
pygame.display.set_caption("Pygame Yersultan")

icon = pygame.image.load('images/ps.png')
pygame.display.set_icon(icon)

square = pygame.Surface((140, 159))
square.fill((53, 92, 156))

ps = pygame.image.load("images/ps.png")
myfont = pygame.font.Font('fonts/BigShoulder.ttf', 50)
text_surface = myfont.render("yearsoultown's ps", True, "Black")

running = True
is_purple = True
color = (104, 73, 171)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_purple = not is_purple
            
            if is_purple:
                color = (104, 73, 171)
            else:
                color = (171, 73, 73)

    screen.fill('White')
    
    screen.blit(square, (100, 40))
    screen.blit(ps, (105, 60))
    screen.blit(text_surface, (70, 180))
    
    pygame.draw.circle(ps, 'Blue', (0, 0), 45)
    pygame.draw.circle(ps, 'Blue', (120, 0), 45)
    pygame.draw.circle(ps, 'Blue', (0, 140), 45)
    pygame.draw.circle(ps, 'Blue', (120, 140), 45)
    
    
    pygame.draw.rect(screen, color, pygame.Rect(0, 470, 1000, 60))
    pygame.draw.rect(screen, color, pygame.Rect(0, -30, 1000, 60))
    
    pygame.display.update()
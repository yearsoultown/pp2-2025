import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

x, y, radius = 20, 20, 19

running = True

while running:
    
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, "Red", (x, y), radius)
    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_w] and y - radius > 0:
        y -= 20
    if pressed[pygame.K_s] and y + radius < 500:
        y += 20
    if pressed[pygame.K_d]and x + radius < 500:
        x += 20
    if pressed[pygame.K_a] and x - radius > 0: 
        x -= 20
    
    
    
    pygame.display.update()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    
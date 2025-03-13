import pygame

pygame.init()

screen = pygame.display.set_mode((900, 960))
pygame.display.set_caption("another game")

icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

effect = pygame.mixer.music.load('sound_effects/sound.wav')
pygame.mixer.music.play(-1)
running = True

x = 30
y = 30

clock = pygame.time.Clock()
ball = pygame.image.load('images/ball.png')



while running:
    
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] : y -= 3
    elif pressed[pygame.K_DOWN] : y += 3
    elif pressed[pygame.K_RIGHT] : x += 3
    elif pressed[pygame.K_LEFT] : x -= 3
    elif pressed[pygame.K_r] : x , y = 450, 430
        
    
    screen.blit(ball, (x,y))
    
    
    clock.tick(60)
    
    pygame.display.update()
import pygame

pygame.init()

screen = pygame.display.set_mode((612, 382))

pygame.display.set_caption('my own program')

icon = pygame.image.load('images/ps.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png')

pygame.mixer.music.load('sound_effects/sound.wav')
pygame.mixer.music.play(-1)


clock = pygame.time.Clock()

x,y = 30, 30

walk_right = [
    pygame.image.load('player right/1.png'),
    pygame.image.load('player right/2.png'),
    pygame.image.load('player right/3.png'),
    pygame.image.load('player right/4.png')
]

walk_left = [
    pygame.image.load('player left/-1.png'),
    pygame.image.load('player left/-2.png'),
    pygame.image.load('player left/-3.png'),
    pygame.image.load('player left/-4.png')
]

player_anim_count = 0

bg_x = 0

running = True

while running:
    
    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x + 682,0))
    screen.blit(walk_right[player_anim_count], (280, 250))
    
    
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1
        
    bg_x -= 2
    if bg_x == -682:
        bg_x = 0
        
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    clock.tick(10)
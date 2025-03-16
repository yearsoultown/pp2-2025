import pygame

pygame.init()
pygame.mixer.init()

pygame.display.set_mode((500, 500))

playlist = ['sound_effects/sound.wav', 'sound_effects/music2.wav']
current_song = 0  

def play_song():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play(-1)

def next_song():
    global current_song
    current_song = (current_song + 1) % len(playlist)
    play_song()

def previous_song():
    global current_song
    current_song = (current_song - 1) % len(playlist)
    play_song()

play_song()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                play_song()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_d:
                next_song()
            elif event.key == pygame.K_a:
                previous_song()

pygame.quit()

import datetime
import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Часики Микки")


clock_face = pg.image.load("images/mickey.png") 
clock_face = pg.transform.scale(clock_face, (600, 600))

minute_hand = pg.image.load("images/righthand.png") 
minute_hand = pg.transform.scale(minute_hand, (40, 500))

second_hand = pg.image.load("images/lefthand.png")  
second_hand = pg.transform.scale(second_hand, (40, 500))

clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

  
    my_time = datetime.datetime.now()
    minuteRN = my_time.minute
    secondRN = my_time.second

    
    angleMin = - (minuteRN * 6) - 10
    angleSec = - (secondRN * 6) - 5

    rotated_minute = pg.transform.rotate(minute_hand, angleMin)
    rotated_second = pg.transform.rotate(second_hand, angleSec)

    
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (100, 100))

   
    screen.blit(rotated_minute, (400 - rotated_minute.get_width() // 2, 400 - rotated_minute.get_height() // 2))
    screen.blit(rotated_second, (400 - rotated_second.get_width() // 2, 400 - rotated_second.get_height() // 2))

    
    pg.display.flip()
    clock.tick(50)


pg.quit()

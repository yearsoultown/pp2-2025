import pygame
import psycopg2

conn = psycopg2.connect("dbname=snake_game user=postgres password = 1234")
cur = conn.cursor()

from random import randint, randrange
pygame.init()

size = width, height = 1050, 650
block = 25
x, y = randrange(block, width - block, block), randrange(block, height - block, block)
apple =  randrange(block, width - block, block), randrange(block, height - block, block)
dirs = {'UP': True, 'DOWN': True, 'RIGHT': True, 'LEFT': True}
length = 1
score = 0
snake = [(x, y)]
dx, dy = 0, 0
fps = 7
Level = 0
started = False


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_menu = pygame.font.Font('font.ttf', 85)
font_menu_user = pygame.font.Font('font.ttf', 40)
font_totalscore = pygame.font.SysFont('Arial', 25, bold=True)
font_level = pygame.font.SysFont('Arial', 26 , bold = True )
font_levelshow = pygame.font.SysFont('Arial', 26, bold = True)
game_background = pygame.image.load('game_background.jpg').convert()
menu_background = pygame.image.load('menu_background.jpg').convert()

DONDO = pygame.USEREVENT + 1
pygame.time.set_timer(DONDO, 5000)


def get_username():
    input_text = ""
    entering = True
    while entering:
        screen.blit(menu_background, (0, 0))
        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))
        user_menu = font_menu_user.render('Enter username and press Enter', True, pygame.Color('black'))
        screen.blit(render_menu, (430, 550))
        screen.blit(user_menu, (300, 460))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text.strip() != "":
                    return input_text.strip()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        input_surface = font_menu_user.render(input_text, True, pygame.Color('black'))
        screen.blit(input_surface, (400, 500))
        pygame.display.flip()


class Wall:
  def __init__(self):
    self.body = []
    self.load_wall()

  def load_wall(self):
    walls = 'Wall{}.txt'
    if Level <= 2: 
        with open(walls.format(str(Level + 1)), 'r') as f:
            f = f.readlines()

        for i, line in enumerate(f):
            for j, value in enumerate(line):
                if value == '#':
                    self.body.append([j, i])

  def draw(self):
    for x, y in self.body:
      pygame.draw.rect(screen, RED, (x * block, y * block, block, block))


def main_menu():
    menu = True
    while menu:
        screen.blit(menu_background, (0, 0))

        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))
        user_menu = font_menu_user.render('Press Enter to start', True, pygame.Color('black'))
        screen.blit(render_menu, (430, 550))
        screen.blit(user_menu, (300, 460))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                global user, record
                user = get_username()
                cur.execute("SELECT score FROM public.snake WHERE name = %s;", (user,))
                record = cur.fetchone()
                menu = False

        pygame.display.flip()


wall = Wall()
main_menu()

food_number = 0

while True:
    screen.blit(game_background, (0, 0))

    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))

    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screen.blit(render_score, (20, 20))
    render_level = font_level.render(f'Level: {Level}', True, pygame.Color('black'))
    screen.blit(render_level,(930, 20))

    if started:
        x += dx * block
        y += dy * block
        snake.append((x, y))
        snake = snake[-length:]

        if x < block or x > width - 2 * block or y < block or y > height - 2 * block or len(snake) > len(set(snake)):
            while True:
                render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
                screen.blit(render_end, (335, 300))
                render_totalscore = font_totalscore.render(f'Total score: {score}' , True, pygame.Color('white'))
                screen.blit(render_totalscore, (345,365))
                render_levelshow = font_levelshow.render(f'Level: {Level}', True, pygame.Color('white'))
                screen.blit(render_levelshow, (345,390))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        if record != None: 
                            cur.execute("DELETE FROM public.snake WHERE name = %s;", (user,))
                            conn.commit()
                            cur.execute("INSERT INTO public.snake(name, score) VALUES (%s, %s);", (user, score + record[0]))
                            conn.commit()
                        else: 
                            cur.execute("INSERT INTO public.snake(name, score) VALUES (%s, %s);", (user, score))
                            conn.commit()
                        print("insert completed")
                        exit()

        if snake[-1] == apple:
            while apple in snake:
                apple = randrange(block, width - block, block), randrange(block, height - block, block)
            length += 1
            score += randint(1, 3)
            food_number += 1
            if food_number == 4:
                Level += 1
                wall.load_wall()
                fps += 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == DONDO:
            if food_number == 4:
                apple = randrange(block, width - block, block), randrange(block, height - block, block)
                food_number = 0

    wall.draw()
    pygame.display.flip()
    clock.tick(fps)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and dirs['UP']:
        dx, dy = 0, -1
        dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
        started = True
    if key[pygame.K_DOWN] and dirs['DOWN']:
        dx, dy = 0, 1
        dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
        started = True
    if key[pygame.K_LEFT] and dirs['LEFT']:
        dx, dy = -1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
        started = True
    if key[pygame.K_RIGHT] and dirs['RIGHT']:
        dx, dy = 1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
        started = True

import pygame, sys, random, time


def movement():
    global play, snake_length
    pos_x = []
    pos_y = []
    if (snake_list[0].bottom > screen_height) or(snake_list[0].top < 0) or (snake_list[0].right > screen_width) or (snake_list[0].left < 0):
        play = False

    if left:
        snake_list[0].x -= move_speed
    elif right:
        snake_list[0].x += move_speed
    elif up:
        snake_list[0].y -= move_speed
    elif down:
        snake_list[0].y += move_speed

    for a in range(snake_length):
        pos_x.append(snake_list[a].x)
        pos_y.append(snake_list[a].y)

    for a in range(1, snake_length):
        snake_list[a].x, snake_list[a].y = pos_x[a-1], pos_y[a-1]


def setup():
    global move_speed
    global play
    global left, right, up, down
    global snake_list
    global snake_length
    global snake_list
    global snake_list
    move_speed = 40
    play = True
    left, right, up, down = False, False, False, False
    snake_list = []
    snake_length = 2
    snake_list.append(head)
    snake_list.append(pygame.Rect(screen_width / 2 - 20, screen_height / 2 - 20, 40, 40))
    head.x, head.y = screen_width/2-20, screen_height/2-20


def draw():
    screen.fill(bg_color)
    sc = score.render(f"{snake_length - 2}", True, (40, 40, 40))
    screen.blit(sc, (200, 125))
    for x in snake_list:
        if x == head:
            pygame.draw.rect(screen, green, x)
        else:
            pygame.draw.rect(screen, white, x)
    pygame.draw.rect(screen, red, fruit)


#                                                                       <=SETUP=>
pygame.init()

clock = pygame.time.Clock()
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snake")

#                                                                       <=variable=>
fruitX, fruitY = random.randrange(15)*40, random.randrange(15)*40
fruit = pygame.Rect(fruitX, fruitY, 40, 40)
head = pygame.Rect(screen_width/2-20, screen_height/2-20, 40, 40)

move_speed = 40
play = True
left, right, up, down = False, False, False, False
#                                                                       <=text=>
score = pygame.font.SysFont('Arial', 300)
game_over = pygame.font.SysFont('Arial', 100)
text = pygame.font.SysFont('Arial', 40)
end_score = pygame.font.SysFont('Arial', 20)

snake_list = []
snake_length = 2
snake_list.append(head)
snake_list.append(pygame.Rect(screen_width/2-20, screen_height/2-20, 40, 40))

#                                                                       <=color=>
bg_color = pygame.Color("grey12")
white = (220, 220, 220)
red = (255, 30, 30)
green = (30, 255, 30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                left, right, up, down = False, False, True, False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                left, right, up, down = False, False, False, True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                left, right, up, down = True, False, False, False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                left, right, up, down = False, True, False, False
            elif event.key == pygame.K_r:
                setup()
    if play:
        movement()
        for x in range(2, snake_length):
            if head.colliderect(snake_list[x]):
                play = False

        if head.colliderect(fruit):
            snake_length += 1
            fruit.x, fruit.y = random.randrange(15) * 40, random.randrange(15) * 40
            while True:
                can = True
                for x in range(snake_length):
                    if fruit.colliderect(snake_list[x-1]):
                        fruit.x, fruit.y = random.randrange(15) * 40, random.randrange(15) * 40
                        can = False
                if can:
                    break

            snake_list.append(pygame.Rect(head.x, head.y, 40, 40))
        draw()
    else:
        text1 = game_over.render("GAME OVER", True, (255, 255, 255))
        text2 = text.render("Press R to restart.", True, (255, 255, 255))
        text3 = end_score.render("Your score is " + str(snake_length-2) + ".", True, (255, 255, 255))
        screen.blit(text1, (50, 150))
        screen.blit(text2, (175, 300))
        screen.blit(text3, (250, 350))

    time.sleep(.2)
    pygame.display.flip()
    clock.tick(60)
import pygame
import random
import os
pygame.mixer.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
pygame.init()

screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))

#background image
bgimg=pygame.image.load("bg.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

#game title
pygame.display.set_caption("Snake se chill")
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow,color,snk_lst,snake_size):
    for x,y in snk_lst:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
def welcome_screen():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimg, (0, 0))
        text_screen("Welcome to Snakes BC",black,260,250)
        text_screen("Press space bar to play", black, 260, 290)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('Mast Nazron Se.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)





def gameloop():
    #game specification
    exit_game=False
    game_over=False
    snake_x= 45
    snake_y= 55
    snake_size= 30

    init_velocity=5
    fps=60
    velocity_x=0
    velocity_y=0
    score=0
    food_x=random.randint(20,screen_width/1.5)
    food_y=random.randint(20,screen_height/1.5)
    snk_lst=[]
    snk_length=1
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill((233,210,222))
            text_screen('''Game over:) press enter to continue''',red,120,250)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome_screen()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    if event.key==pygame.K_q:
                        score+=10
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                snk_length+=5
                food_x = random.randint(20, screen_width / 1.5)
                food_y = random.randint(20, screen_height / 1.5)
                if int(hiscore)<score:
                    hiscore=score

            gameWindow.fill(white)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)
            if len(snk_lst)>snk_length:
                del snk_lst[0]
            if head in snk_lst[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
        #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_lst,snake_size)
            text_screen("score: " + str(score )+" High Score: "+ str(hiscore), red, 5, 5)
        pygame.display.update()
        clock.tick(fps)




    pygame.quit()
    quit()
welcome_screen()

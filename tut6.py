import pygame
pygame.init()

gamewindow=pygame.display.set_mode((1200,500))#display window
pygame.display.set_caption("My First Game-BLANK")#name of dispay window
#game specification
exit_game=False
game_over=False
#game looop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("you have pressed right ")


pygame.quit()
quit()

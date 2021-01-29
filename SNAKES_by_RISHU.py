import pygame #game ko initialize kiye h
import random #randomizer h python ka
import os #highscore.txt file bnane k liye

pygame.mixer.init()
pygame.mixer.music.load('mixkit-suspense-mystery-bass-685.mp3')
pygame.mixer.music.play()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow1 =(15, 240, 0)
yellow =(255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
magenta = (205, 0, 105)

# CONSOLE WINDOW BANNANE K LIYE
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))


# bg ImportWarning
bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()



# Game ka Title
pygame.display.set_caption("-NOKIA 3310wala - _SNAKES_--- by R-Enterprises")
pygame.display.update()

ghari = pygame.time.Clock()


# predefinded FONTS K LIYE jiska size appanne 55 set kiye h
font = pygame.font.SysFont(None,55)

# pygame KA DOCUMENTATIONS CHECK KIYOOO
def screen_pr_score(text, color, x, y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_saanp(gameWindow, color,saanp_list, saanp_size):
    # print(saanp_list)
    for x,y in saanp_list:
        pygame.draw.rect(gameWindow, color, [x, y, saanp_size, saanp_size])

# adding welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        screen_pr_score("Welcome to Snakes",black, 260,270)
        screen_pr_score("Press SPACEBAR to Play",yellow1, 210,530)
        screen_pr_score("********* R-Enterprises *********",red, 170,80)
        # # snack.jpg file ko upload kiye
        # gameWindow.blit(bgimg1,(0 ,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()

                    gameloop()


        pygame.display.update()
        ghari.tick(30)
        

# Game Loop
def gameloop():

    # Game k kuch specific variables

    # for game loop
    exit_game = False
    game_over = False

    saanp_x = 45
    saanp_y = 55

    # khane ka saamaan wale variables
    khana_x = random.randint(25, screen_width/1.5)
    khana_y = random.randint(25, screen_height/1.5)

    # apna score wala variable
    point = 0

    # SAPOLE KI VELOCITY K LIYE
    velocity_x = 0
    velocity_y = 0
    badhti_hui_velocity = 5

    # while increasing the size munddi has to be cut at the same time
    saanp_list = []
    saanp_length = 1

    # pehle check krenge ki highscore wali file pehle se exsist kr bhi rhi h ya nhi
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    # READING the highscore file :::highscore.txt
    with open("highscore.txt", "r") as f:
        highscore=f.read()

    saanp_size = 20

    # GAME KA FRAME CHANGING RATE
    fps = 30 
    # ^^---AGER TERE PASS ACHA WALA DISPLAY H to)FPS WALA TO BADHA LENA 30  se  60 fps kr liyoo

    while not exit_game:


        # GAMEOVER krne k liye naya loop
        if game_over:
            # READING the highscore file :::highscore.txt
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(magenta)
            screen_pr_score("GAME OVER!! Press Enter to Restart", yellow, 100, 250)
            screen_pr_score("Score: " + str(point) + "  Highscore : " + str(highscore),yellow ,200,340)
            # print("UR SCORE IS : ", point)


            for event in pygame.event.get():                   #<<<<<<<<<<<<<<<<<vv
                if event.type == pygame.QUIT:                                   #^^
                    exit_game = True # game se exit krne k liye^                #^^
                                                                                #^^
                if event.type == pygame.KEYDOWN:#key strocks catch krne k liye  #^^
                    if event.key == pygame.K_RETURN:                            #vv
                        welcome()
                                                                      #vv
                                                                                #vv
                                                                                #vv
        else:                                                                   #vv
            for event in pygame.event.get():       #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<vv
                if event.type == pygame.QUIT:
                    exit_game = True # game se exit krne k liye

                if event.type == pygame.KEYDOWN:#key strocks catch krne k liye

                    if event.key == pygame.K_RIGHT:#rightaerokey k liye function
                        velocity_x = badhti_hui_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:#LEFTaerokey k liye function
                        velocity_x = -badhti_hui_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:#UPaerokey k liye function
                        velocity_y = - badhti_hui_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:#DOWNaerokey k liye function
                        velocity_y = badhti_hui_velocity
                        velocity_x = 0
                    # cheatcode
                    if event.key == pygame.K_q:
                        point+= 10             #increase point 
                    if event.key == pygame.K_a:
                        point+= -10            #decrease point 
                    if event.key == pygame.K_w:
                        badhti_hui_velocity +=3#increase velocity 
                    if event.key == pygame.K_s:
                        badhti_hui_velocity -=3#decrease velocity 

            # sapoole ki gatiwidhiyoon me badlaaw k liyee
            saanp_x = saanp_x + velocity_x
            saanp_y = saanp_y + velocity_y

            # is loop me saapolla apna khaa leta h n thenn re set ho jata hasattr
            if abs (saanp_x - khana_x)<25 and abs(saanp_y-khana_y)<25:
                point+=10
                print("POINT = ",point)

                # sab kuch over lap na hojaaye issiliye ye rewrite boleto overwrite stament avoid kiye 
                khana_x = random.randint(25, screen_width/1.5)
                khana_y = random.randint(25, screen_height/1.5)

                saanp_length +=4
                # print("HIGH SCORE : ", highscore)
                if point> int(highscore):
                    highscore=point


        # or yaha apna loop hota h khtm
            gameWindow.fill(black)#console bgcolor

            # snack.jpg file ko upload kiye
            gameWindow.blit(bgimg,(0 ,0))
            
            

        # score ko display kr waya h console pr
            screen_pr_score("Score: " + str(point) ,red ,5,5)
            # saapoole ka orientation#
            pygame.draw.rect(gameWindow, white, [khana_x, khana_y, saanp_size, saanp_size])

            saanp_ki_munddi = []
            saanp_ki_munddi.append(saanp_x)
            saanp_ki_munddi.append(saanp_y)
            saanp_list.append(saanp_ki_munddi)

        #***********************************************

        # saapoole ki 0th boleto zeroth element to kaat te rehna h 
            if len(saanp_list)>saanp_length:
                del saanp_list[0]

        # **************************************************

        # ager saapoole ki mundi uske baki k body part se touch ho tb GAME OVER
            if saanp_ki_munddi in saanp_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
        #  *****************************************************

        # GAMEOVER K LIYE NAYA FUNCTIonality boundary me ja k ager lard gaya tb liye
            if saanp_x<0 or saanp_y<0 or screen_height<saanp_y or screen_width<saanp_x:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                print("GAME OVER")

        #********************************************************

            # pygame.draw.rect(gameWindow, red, [saanp_x, saanp_y, saanp_size, saanp_size])
            plot_saanp(gameWindow, red, saanp_list, saanp_size)


        # apne display ko refresh kiya 
        pygame.display.update()

        # finally ghari ki fps set kri hasattr
        ghari.tick(fps)


    pygame.quit()
    quit()
welcome()

import pygame
import time
from pygame.locals import *
import random


pygame.init()

#Fill Colors // Used for backgrounds and Texts
fWhite =(255,255,255)
fRed = (255,000,000)
fGreen = (0 , 105 , 0)
bGreen = (0 , 255 , 0)
ecSnake = (0,155,0)
fGray = (105,105,105)
bGray = (192,192,192)
fBlack = (0,0,0)

#Entity Colors // Used for entities 
ecSnake = (0,155,0)

#Variables // d = Dispplay Pixels
d_Width = 800
d_Height = 600 
d_Blocks = 20

#Musics
gamemusic = pygame.mixer.Sound('Gamefiles/gamesong.ogg')
#Sprites
SnakeHead00 = pygame.image.load('Gamefiles/SHead00.png')
STail00 = pygame.image.load('Gamefiles/STail00.png')
displaybackground = pygame.image.load('Gamefiles/background.png')
gicon = pygame.image.load('Gamefiles/gameicon.png')
startbackground = pygame.image.load('Gamefiles/StartBackground.png')
imgapple = pygame.image.load('Gamefiles/Holywaterapple.png')

pygame.display.set_icon(gicon)


direction = "right"
tdirection = "right"
gDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('God\'s Serpent')

FPS = 15   
smallfont = pygame.font.Font("Gamefiles/scaryfont.ttf" , 25)
mediumfont = pygame.font.Font("Gamefiles/scaryfont.ttf" , 50)
largefont = pygame.font.Font("Gamefiles/scaryfont.ttf" , 150)# Font Style
pbutton = pygame.font.Font("Gamefiles/playgamebutton.otf" , 20)


TZ = pygame.time.Clock() 
#Functions   
def pause():

    

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        dMessage("PAUSED" , fWhite , -100 , size="large")
        dMessage("press c to continue or q to quit" , fWhite ,25)
    
        pygame.display.update()
        TZ.tick(5)

    

def score(score):
    txt = mediumfont.render("Score: " + str(score) , True , fWhite)
    gDisplay.blit(txt, [0,0])

    
def SpawnApple():
    d_Apple_x = round(random.randrange(0 , d_Width - d_Blocks)) 
    d_Apple_y = round(random.randrange(0 , d_Height - d_Blocks))

    return d_Apple_x , d_Apple_y


    

    
def start_menu():
    smenu = True


    while smenu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

                                
        gDisplay.blit(startbackground , [0,0])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(gDisplay , fGray , (550,450,100,50))
        #The most ghetto way ive ever done in to my code        
        if 150 + 100  > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gDisplay , bGreen , (150,450,100,50))
            if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
                if click[0] == 1:
                    StartGame()
                    
        else:
            pygame.draw.rect(gDisplay , fGreen , (150,450,100,50))
            
        if 550 + 100 > mouse [0] > 500 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gDisplay , bGray , (550,450,100,50))
            
            if 550+100 > mouse[0] > 500 and 450 + 50 > mouse[1]>450:
                if click[0] == 1:
                    pygame.quit()
                    quit()

                    

                    
                
##        if 550+100 > mouse[0] > 500 and 450+50 > mouse[1] > 450:
##        pygame.draw.rect(gDisplay , fGray , (550,450,100,50))
##        if 550+100 > mouse[0] > 500 and 450 + 50 > mouse[1] > 450:
##             pygame.draw.rect(gDisplay , bGray , (550,450,100,50))                      
#Ghetto Coding LOL! the dirtiest trick ive done to fit it inside the play box this is disgusting start of my programming career
            
        dMessage("Play                                        " , fBlack , y_dis=175  , size="mediumButton")
        dMessage("                                        Quit" , fBlack , y_dis=175  , size="mediumButton")

       # pygame.draw.rect(gDisplay , fGray , (550,450,100,50))
        dMessage("                                        Quit" , fBlack , y_dis=175  , size="mediumButton")

        pygame.display.update()
        TZ.tick(15)
        

def txt_objects(text,color,size):
    if size == "small":       
        textSurface = smallfont.render(text , True , color)
    elif size == "medium":       
        textSurface = mediumfont.render(text , True , color)
    elif size == "mediumButton":
        textSurface = pbutton.render(text , True , color)
    elif size == "large":       
        textSurface = largefont.render(text , True , color)
    return textSurface , textSurface.get_rect()

def dMessage(msg , color , y_dis=0 , size="small"):
    textSurf , textRect = txt_objects(msg,color, size)
    textRect.center = (d_Width / 2) , (d_Height / 2) + y_dis
    gDisplay.blit(textSurf , textRect)

#    dText = FStyle.render(msg , True , color)
#    gDisplay.blit(dText , [d_Width / 2 , d_Height / 2])

                       
def Serpent(d_Blocks , SList):

    if direction == "right":
        SHead = pygame.transform.rotate(SnakeHead00 , 270)
    if direction == "left":
        SHead = pygame.transform.rotate(SnakeHead00 , 90)
    if direction == "up":
        SHead = SnakeHead00
    if direction == "down":
        SHead = pygame.transform.rotate(SnakeHead00 , 180)


    if tdirection == "right":
        STail = pygame.transform.rotate(STail00 , 270)
    if tdirection == "left":
        STail = pygame.transform.rotate(STail00 , 90)
    if tdirection == "up":
        STail = STail00
    if tdirection == "down":
        STail = pygame.transform.rotate(STail00 , 180)

    
     

    gDisplay.blit(SHead , (SList[-1][0] , SList[-1][1]))
    gDisplay.blit(STail00 ,(SList[0][0],SList[0][1]))

    for XY in SList[:-1]:
        pygame.draw.rect(gDisplay , ecSnake , [XY[0],XY[1],d_Blocks,d_Blocks])
        gDisplay.blit(STail00 ,(SList[0][0],SList[0][1] , d_Blocks , d_Blocks))
##    for XnY in SList[0]:
##        gDisplay.blit(STail00 ,(SList[0][0],SList[0][1]))

    


def StartGame():
    pygame.mixer.Sound.play(gamemusic)
    gExit = False
    gOver = False
    global direction
    direction = "right"
    global tdirection
    
    GP_x = d_Width / 2  
    
    GP_y = d_Height / 2 
    
    GP_x_m = 20 
    
    GP_y_m = 0 

    SList = []

    SLength = 2

    d_Apple_x , d_Apple_y = SpawnApple()
  

 
    while not gExit:

               
        while gOver == True:
            gDisplay.fill(fBlack)
            dMessage("You Died", fRed , -50 , size="large")
            dMessage("Remember Jesus died for your sin , Try again", fRed , 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gExit = True
                    gOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gExit = True
                        gOver = False
                    if event.key == pygame.K_c:
                        StartGame()
            
                                            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    tdirection = "left"
                    GP_x_m = - d_Blocks 
                    GP_y_m = 0
                    
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    tdirection = "right"
                    GP_x_m = d_Blocks 
                    GP_y_m = 0
                        
                elif event.key == pygame.K_UP:
                    direction = "up"
                    tdirection = "up"
                    GP_y_m = - d_Blocks 
                    GP_x_m = 0
                    
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    tdirection = "down"
                    GP_y_m = d_Blocks 
                    GP_x_m = 0

                elif event.key == pygame.K_p:
                    pause()
                    
        if GP_x >= d_Width  or GP_x < 0 or GP_y >= d_Height or GP_y < 0:
                gOver = True
                
        #Game Structs
                
        GP_x += GP_x_m
        GP_y += GP_y_m
        gDisplay.blit(displaybackground , [0,0])
        d_Apple_Thickness = 30
        gDisplay.blit(imgapple, (d_Apple_x , d_Apple_y))
        SHead = []
        SHead.append(GP_x)
        SHead.append(GP_y)
        SList.append(SHead)

        if len(SList) > SLength:
            del SList[0]

        for eachPixel in SList[:-1]:
            if eachPixel == SHead:
                gOver = True

       
        
                
        Serpent(d_Blocks , SList )

        score(SLength-2)
        pygame.display.update()


        if GP_x > d_Apple_x and GP_x < d_Apple_x + d_Apple_Thickness or GP_x + d_Blocks > d_Apple_x and GP_x + d_Blocks < d_Apple_x + d_Apple_Thickness:
            if GP_y > d_Apple_y and GP_y < d_Apple_y + d_Apple_Thickness or GP_y + d_Blocks > d_Apple_y and GP_y + d_Blocks < d_Apple_y + d_Apple_Thickness:
                d_Apple_x , d_Apple_y = SpawnApple()
                SLength += 1
                
            elif GP_y + d_Blocks > d_Apple_y and GP_y + d_Blocks < d_Apple_y + d_Apple_Thickness:
                d_Apple_x , d_Apple_y = SpawnApple()
                SLength += 1
                
            
        
        
        TZ.tick(FPS)
                
       
    pygame.quit()
    quit()

start_menu()
StartGame()


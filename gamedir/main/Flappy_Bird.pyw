#modules
import pygame
from random import randint
from tkinter import *
import time


#various color codes utilized
black = (0,0,0)
white = (255,255,255)
grey = (211,211,211)
grey2 = (169,169,169)
green = (0,255,0)
red = (255,0,0)
blue = (51, 91, 255)
blue2 = (20, 40, 150)
yellow = (255,255,0)
yellow2 = (100,160,100)

pygame.init() #initialize the module

size = 1680,1050 #native res
screen = pygame.display.set_mode(size) #apply size to canvas
pygame.display.set_caption("Flappy Bird") #caption name 

done = False
clock = pygame.time.Clock()

#functions that apply to variables
def ball(x,y):
    pygame.draw.circle(screen,yellow,[x,int(y)], 12)
    pygame.draw.circle(screen,yellow,[int(x+16),int(y-10)], 8)
    pygame.draw.circle(screen,blue2,[int(x),int(y+4)], 8)
    pygame.draw.circle(screen,black,[int(x+18),int(y-10)], 2)
    pygame.draw.circle(screen,red,[int(x+16),int(y-18)], 4)
    pygame.draw.circle(screen,blue2,[int(x-14),int(y+1)], 4)
    pygame.draw.circle(screen,yellow2,[int(x+25),int(y-11)], 4)
    

def gameover():
    font = pygame.font.SysFont(None, 75)
    text = font.render("Game Over", True, red)
    screen.blit(text, [680, 525])

def obstacle(xcloc, ycloc, xsize, ysize):
    pygame.draw.rect(screen, green, [xcloc, ycloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xcloc, int(ycloc+ysize+space), xsize, ysize+950])

def cloud(clx, cly):
    pygame.draw.circle(screen, grey2, [int(clx),int(cly)],20)
    pygame.draw.circle(screen, grey2, [int(clx +30),int(cly-10)],20)
    pygame.draw.circle(screen, grey, [int(clx+30),int(cly)],20)
    pygame.draw.circle(screen, grey2, [int(clx+30),int(cly+10)],20)
    pygame.draw.circle(screen, grey2, [int(clx+50),int(cly+10)],20)
    
def Score(score):
    font = pygame.font.SysFont(None, 75)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [0,0])

#variables/dimensions
x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 1050
xcloc = 1400
ycloc = 0
xsize = 70
ysize = randint(0, 350)
space = 150
obspeed = 2.5
score = 0

#keyboard events 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -6
                file1 = ('C:\\Users\\kevsi\\Desktop\\gamedir\\ingamesounds\\Jump.wav')
                root = Tk()
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(file1)
                pygame.mixer.music.play()
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 4

    
    screen.fill(blue)#bg will be the "blue" variable
    
    cloud(900, 500)
    cloud(700, 550)
    cloud(500, 500)
    cloud(600, 500)
    cloud(400, 600)
    cloud(300, 750)
    cloud(200, 500)
    cloud(100, 500)
    cloud(1000, 550)
    cloud(1050, 500)
    cloud(1200, 560)
    cloud(1300, 540)
    cloud(1400, 550)
    cloud(1450, 500)
    cloud(1600, 540)
    cloud(50, 520)
    cloud(100, 950)
    cloud(1100, 500)
    cloud(1050, 500)
    cloud(1200, 760)
    cloud(1300, 840)
    cloud(1000, 850)
    cloud(1450, 800)
    cloud(1500, 970)
    cloud(1600, 940)
    cloud(50, 520)
    cloud(1100, 100)
    cloud(1050, 100)
    cloud(1200, 160)
    cloud(1300, 240)
    cloud(1000, 250)
    cloud(1450, 200)
    cloud(1500, 170)
    cloud(1600, 240)
    cloud(50, 120)
    
 
    obstacle(xcloc, ycloc, xsize, ysize)#green obstacles
    ball(x,y)#ball
    Score(score)#score
#speed as keyboard events are inputted into the software    
    y += y_speed
    xcloc -= obspeed

#conditions


    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0
        file2 = ('C:\\Users\\kevsi\\Desktop\\gamedir\\ingamesounds\\Jump14.wav')
        root = Tk()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file2)
        pygame.mixer.music.play()
        time.sleep(2)
    
    if x+20 > xcloc and y-20 < ysize and x-15 < xsize+xcloc:
        gameover()
        obspeed = 0
        y_speed = 0
        file3 = ('C:\\Users\\kevsi\\Desktop\\gamedir\\ingamesounds\\Jump14.wav')
        root = Tk()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()
        time.sleep(2)
        
            
    if x+20 > xcloc and y+20 > ysize+space and x-15 < xsize+xcloc:
        gameover()
        obspeed = 0
        y_speed = 0
        file4 = ('C:\\Users\\kevsi\\Desktop\\gamedir\\ingamesounds\\Jump14.wav')
        root = Tk()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file4)
        pygame.mixer.music.play()
        time.sleep(2)
        

    if xcloc < -80:
        xcloc = 700
        ysize = randint(0,350)

    if x > xcloc and x < xcloc+3:
        score = (score + 1)
        file5 = ('C:\\Users\\kevsi\\Desktop\\gamedir\\ingamesounds\\Pickup_Coin2.wav')
        root = Tk()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file5)
        pygame.mixer.music.play()
       
    pygame.display.flip()
    clock.tick(60)

#exit
pygame.quit()


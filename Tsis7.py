import pygame
import math
import time
#pylint: disable=no-member
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (750,495)
width = 750
height = 450
A = 200
freq = 3
speed = 0.5
fontz = pygame.font.Font(None, 20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SIN$$COS")
surface = pygame.Surface((width, height))
surface.fill(WHITE)
run = True
n = 1
while run:
    screen.fill(WHITE)
    pygame.draw.line(screen, (BLACK), (0,225), (16, 225),2) 
    screen.blit(fontz.render("0.00", True, (BLACK)),(22,225)) 


    pygame.draw.line(screen, (BLACK), (0,23), (16,23),2) 
    screen.blit(fontz.render("1.00", True, (BLACK)),(22,23))

    pygame.draw.line(screen, (BLACK), (0,73), (16,73),2) 
    screen.blit(fontz.render("0.75", True, (BLACK)),(22,73))

    pygame.draw.line(screen, (BLACK), (0,123), (16,123),2) 
    screen.blit(fontz.render("0.50", True, (BLACK)),(22,123))

    pygame.draw.line(screen, (BLACK), (0,173), (16,173),2) 
    screen.blit(fontz.render("0.25", True, (BLACK)),(22,173))

    pygame.draw.line(screen, (BLACK), (0,275), (16,275),2) 
    screen.blit(fontz.render("-0.25", True, (BLACK)),(17,275))

    pygame.draw.line(screen, (BLACK), (0,325), (16,325),2) 
    screen.blit(fontz.render("-0.50", True, (BLACK)),(17,325))

    pygame.draw.line(screen, (BLACK), (0,375), (16,375),2) 
    screen.blit(fontz.render("-0.75", True, (BLACK)),(17,375))
    
    pygame.draw.line(screen, (BLACK), (0,425), (16,425),2) 
    screen.blit(fontz.render("-1.00", True, (BLACK)),(17,425))



    pygame.draw.line(screen, (RED), (560,27), (530,27), 2)
    screen.blit(fontz.render("SIN (X)", True, (BLACK)),(480,23))

    pygame.draw.line(screen, (BLUE), (560,55), (530,55), 2)
    screen.blit(fontz.render("COS (X)", True, (BLACK)),(480,50))
     
    

    

    pygame.draw.line(screen, (BLACK), (51,225), (728,225),3) # X
    pygame.draw.line(screen, (BLACK), (375,3), (375,440),3)  # Y



    pygame.draw.rect(screen, (BLACK), (49, 3, 680, 440),3)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    point = []
    for x in range(50, 728):
        y = int(( height/2 ) + A * math.sin( freq * (( float(x)/width ) * ( 2 * math.pi ) + ( speed * time.time()))))
        
        point.append([x,y])
    pygame.draw.lines(screen, (RED), False, point, 2)
    pointer = []
    
    
    
    for x in range(50, 728):
        y = int(( height/2 ) + A * math.cos( freq * (( float(x)/width ) * ( 2 * math.pi ) + (speed * time.time()))))
        pointer.append([x,y])
    pygame.draw.lines(screen, (BLUE), False, pointer, 2)

    
    
    
    pygame.display.flip()
pygame.quit()
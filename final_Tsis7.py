import pygame
import math
import time
import sys
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
speed = 1
fontz = pygame.font.SysFont('serif', 15)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SIN$$COS")
surface = pygame.Surface((width, height))
surface.fill(WHITE)
run = True
n = 1
while run:
    screen.fill(WHITE)
    #pygame.draw.line(screen, (BLACK), (0,225), (16, 225),2) 
    #screen.blit(fontz.render("0.00", True, (BLACK)),(22,225)) 


    pygame.draw.line(screen, (BLACK), (49,23), (729,23),2) 
    screen.blit(fontz.render("1.00", True, (BLACK)),(12,14))

    pygame.draw.line(screen, (BLACK), (49,73), (729,73),2) 
    screen.blit(fontz.render("0.75", True, (BLACK)),(12,64))

    pygame.draw.line(screen, (BLACK), (49,123), (729,123),2) 
    screen.blit(fontz.render("0.50", True, (BLACK)),(12,114))

    pygame.draw.line(screen, (BLACK), (49,173), (729,173),2) 
    screen.blit(fontz.render("0.25", True, (BLACK)),(12,163))

    pygame.draw.line(screen, (BLACK), (49,275), (729,275),2) 
    screen.blit(fontz.render("-0.25", True, (BLACK)),(9,264))

    pygame.draw.line(screen, (BLACK), (49,325), (729,325),2) 
    screen.blit(fontz.render("-0.50", True, (BLACK)),(9,314))

    pygame.draw.line(screen, (BLACK), (49,375), (729,375),2) 
    screen.blit(fontz.render("-0.75", True, (BLACK)),(9,364))
    
    pygame.draw.line(screen, (BLACK), (49,425), (729,425),2) 
    screen.blit(fontz.render("-1.00", True, (BLACK)),(9,414))



    pygame.draw.line(screen, (RED), (550,40), (520,40), 2)
    screen.blit(fontz.render("sin x", True, (BLACK)),(480,30))

    pygame.draw.line(screen, (BLUE), (550,60), (520,60), 2)
    screen.blit(fontz.render("cos x", True, (BLACK)),(480,50))
     





    pygame.draw.line(screen, (BLACK), (125,443), (125,3),2) 
    screen.blit(fontz.render("-2П", True, (BLACK)),(109,445))

    pygame.draw.line(screen, (BLACK), (249,443), (249,3),2) 
    screen.blit(fontz.render("-П", True, (BLACK)),(239,445))

    pygame.draw.line(screen, (BLACK), (499,443), (499,75),2) 
    screen.blit(fontz.render("П", True, (BLACK)),(495,445))

    pygame.draw.line(screen, (BLACK), (499,5), (499,22),2) 

    pygame.draw.line(screen, (BLACK), (625,443), (625,3),2) 
    screen.blit(fontz.render("2П", True, (BLACK)),(617,445))


    pygame.draw.line(screen, (BLACK), (63,443), (63,429),2) 
    screen.blit(fontz.render("-5П/2", True, (BLACK)),(45,445))

    pygame.draw.line(screen, (BLACK), (73,443), (73,436),1) 
    pygame.draw.line(screen, (BLACK), (93,443), (93,432),1) 
    pygame.draw.line(screen, (BLACK), (113,443), (113,436),1) 
    pygame.draw.line(screen, (BLACK), (133,443), (133,436),1) 
    pygame.draw.line(screen, (BLACK), (153,443), (153,432),1) 
    pygame.draw.line(screen, (BLACK), (173,443), (173,436),1) 

    pygame.draw.line(screen, (BLACK), (193,443), (193,430),2) 
    screen.blit(fontz.render("-3П/2", True, (BLACK)),(178,445))

    pygame.draw.line(screen, (BLACK), (226,443), (226,432),1) 
    pygame.draw.line(screen, (BLACK), (213,443), (213,436),1) 
    pygame.draw.line(screen, (BLACK), (239,443), (239,436),1)




    
    pygame.draw.line(screen, (BLACK), (256,443), (256,437),1) 
    pygame.draw.line(screen, (BLACK), (273,443), (273,433),1) 
    pygame.draw.line(screen, (BLACK), (292,443), (292,437),1)


    pygame.draw.line(screen, (BLACK), (312,443), (312,430),2)
    screen.blit(fontz.render("-П/2", True, (BLACK)),(298,445))


    pygame.draw.line(screen, (BLACK), (329,443), (329,436),1) 
    pygame.draw.line(screen, (BLACK), (347,443), (347,433),1) 
    pygame.draw.line(screen, (BLACK), (363,443), (363,437),1)



#
    pygame.draw.line(screen, (BLACK), (383,443), (383,437),1) 
    pygame.draw.line(screen, (BLACK), (403,443), (403,433),1) 
    pygame.draw.line(screen, (BLACK), (420,443), (420,437),1)


    pygame.draw.line(screen, (BLACK), (436,443), (436,430),2)
    screen.blit(fontz.render("П/2", True, (BLACK)),(426,445))


    pygame.draw.line(screen, (BLACK), (456,443), (456,436),1) 
    pygame.draw.line(screen, (BLACK), (473,443), (473,433),1) 
    pygame.draw.line(screen, (BLACK), (492,443), (492,437),1)


#
    pygame.draw.line(screen, (BLACK), (513,443), (513,437),1) 
    pygame.draw.line(screen, (BLACK), (533,443), (533,433),1) 
    pygame.draw.line(screen, (BLACK), (550,443), (550,437),1)


    pygame.draw.line(screen, (BLACK), (566,443), (566,430),2)
    screen.blit(fontz.render("3П/2", True, (BLACK)),(550,445))


    pygame.draw.line(screen, (BLACK), (586,443), (586,436),1) 
    pygame.draw.line(screen, (BLACK), (603,443), (603,433),1) 
    pygame.draw.line(screen, (BLACK), (618,443), (618,437),1)

#
    pygame.draw.line(screen, (BLACK), (640,443), (640,437),1) 
    pygame.draw.line(screen, (BLACK), (658,443), (658,433),1) 
    pygame.draw.line(screen, (BLACK), (672,443), (672,437),1)


    pygame.draw.line(screen, (BLACK), (685,443), (685,430),2)
    screen.blit(fontz.render("5П/2", True, (BLACK)),(670,445))


    pygame.draw.line(screen, (BLACK), (697,443), (697,436),1) 
    pygame.draw.line(screen, (BLACK), (709,443), (709,433),1) 
    pygame.draw.line(screen, (BLACK), (719,443), (719,437),1)









    

    




    pygame.draw.line(screen, (BLACK), (51,225), (728,225),4) # X
    pygame.draw.line(screen, (BLACK), (375,3), (375,440),4)  # Y



    pygame.draw.rect(screen, (BLACK), (49, 3, 680, 440),4)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
    point = []
    for x in range(50, 728):
        y = int(( height/2 ) + A * math.sin( freq * (( float(x)/width ) * ( 2 * math.pi ) - ( speed * time.time()))))
        
        point.append([x,y])
    pygame.draw.lines(screen, (RED), False, point, 2)
    pointer = []
    
    
    
    for x in range(50, 728):
        y = int(( height/2 ) + A * math.cos( freq * (( float(x)/width ) * ( 2 * math.pi ) - (speed * time.time()))))
        pointer.append([x,y])
    pygame.draw.lines(screen, (BLUE), False, pointer, 2)

    

    
    
    pygame.display.flip()
pygame.quit()
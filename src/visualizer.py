import pygame
import sys

def spawnPygame():
    #inisialisasi pygame
    pygame.init()

    #Warna
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    #setup ukuran layar
    screen = pygame.display.set_mode((800,600))

    #loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        #Update state pygame
                
        screen.fill(WHITE) #layar biru
        pygame.display.flip() #perbarui display
        pygame.time.Clock().tick(60) #FPS = 60
    
    pygame.quit()
    sys.exit()
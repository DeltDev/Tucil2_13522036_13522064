import pygame
import sys


def spawnPygame(ControlPointList):
    #inisialisasi pygame
    pygame.init()
    font = pygame.font.Font(None,25)
    #Warna
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    #setup ukuran layar
    screenHeight = 1920
    screenWidth = 1080
    screen = pygame.display.set_mode((screenHeight,screenWidth))

    #loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        #Update state pygame
                
        screen.fill(WHITE) #layar putih
        #gambar semua control point di pygame
        for i in ControlPointList:
            pygame.draw.circle(screen,BLUE,(i.x,i.y),10) #gambar control point (titik warna biru) (y dibalik karena pygame koordinat y positif arahnya ke bawah)

            text_surface = font.render(f"{i.pointName} ({i.x}, {i.y})", True, BLACK)  # Black color
            text_rect = text_surface.get_rect()
            text_rect.topleft = (i.x + 10, i.y - 20)  # Position the text near the point (y dibalik karena di pygame koordinat y positif arahnya ke bawah)
            screen.blit(text_surface, text_rect)


        pygame.display.flip() #perbarui display
        pygame.time.Clock().tick(60) #FPS = 60
    
    
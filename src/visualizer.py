import pygame
import sys
from point import Point

def spawnPygame(ControlPointList):
    #inisialisasi pygame
    pygame.init()
    font = pygame.font.Font(None,20)
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

    #buat origin baru karena titik origin pertama di pygame di pojok kiri atas
    newOrigin = Point(screenHeight//2,screenWidth//2,"Origin")
    #loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        #Update state pygame
                
        screen.fill(WHITE) #layar putih
        #gambar titik origin
        pygame.draw.circle(screen,BLACK,(newOrigin.x,newOrigin.y),5)
        text_surface = font.render(f"{newOrigin.pointName} ({0}, {0})", True, BLACK) #tandai sebagai titik (0,0)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (newOrigin.x + 10, newOrigin.y - 20) #taruh teks di dekat titik origin
        screen.blit(text_surface, text_rect)
        #gambar semua control point di pygame
        for i in ControlPointList:
             pygame.draw.circle(screen,BLUE,(newOrigin.x + i.x,newOrigin.y-i.y),10) #gambar control point (titik warna biru) (y dibalik karena pygame koordinat y positif arahnya ke bawah)

             text_surface = font.render(f"{i.pointName} ({i.x}, {i.y})", True, BLACK)  # Black color
             text_rect = text_surface.get_rect()
             text_rect.topleft = (newOrigin.x+i.x + 10, newOrigin.y-i.y - 20)  # Position the text near the point (y dibalik karena di pygame koordinat y positif arahnya ke bawah)
             screen.blit(text_surface, text_rect)


        pygame.display.flip() #perbarui display
        pygame.time.Clock().tick(60) #FPS = 60
    
    
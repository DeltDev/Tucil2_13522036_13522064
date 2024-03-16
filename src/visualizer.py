import pygame
import sys
from point import Point

def spawnPygame(ControlPointList):
    #inisialisasi pygame
    pygame.init()
    font = pygame.font.Font(None,20)
    font2 = pygame.font.Font(None,35)
    #Warna
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    #setup ukuran layar
    screenWidth = 1920
    screenHeight = 1080
    screen = pygame.display.set_mode((screenWidth,screenHeight))

    #buat origin baru karena titik origin pertama di pygame di pojok kiri atas
    newOrigin = Point(screenWidth//2,screenHeight//2,"Origin")
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
        originSurface = font.render(f"{newOrigin.pointName} ({0}, {0})", True, BLACK) #tandai sebagai titik (0,0)
        originRect = originSurface.get_rect()
        originRect.topleft = (newOrigin.x + 10, newOrigin.y - 20) #taruh teks di dekat titik origin
        screen.blit(originSurface, originRect)
        #setup koordinat kartesius
        #gambar sumbu x
        pygame.draw.line(screen,BLACK,(0,newOrigin.y),(screenWidth,newOrigin.y),10)
        xSurface = font2.render(f"X", True, BLACK) 
        XRect = xSurface.get_rect()
        XRect.topleft = (screenWidth - 20, newOrigin.y + 10) 
        screen.blit(xSurface, XRect)
        #gambar sumbu y
        pygame.draw.line(screen,BLACK,(newOrigin.x,0),(newOrigin.x,screenHeight),10)
        ySurface = font2.render(f"Y", True, BLACK) 
        yRect = ySurface.get_rect()
        yRect.topleft = (newOrigin.x + 10, 10) 
        screen.blit(ySurface, yRect)
        #gambar semua control point di pygame
        for i in ControlPointList:
             pygame.draw.circle(screen,BLUE,(newOrigin.x + i.x,newOrigin.y-i.y),10) #gambar control point (titik warna biru) (y dibalik karena pygame koordinat y positif arahnya ke bawah)

             text_surface = font.render(f"{i.pointName} ({i.x}, {i.y})", True, BLACK)  # Black color
             text_rect = text_surface.get_rect()
             text_rect.topleft = (newOrigin.x+i.x + 10, newOrigin.y-i.y - 20)  # Position the text near the point (y dibalik karena di pygame koordinat y positif arahnya ke bawah)
             screen.blit(text_surface, text_rect)


        pygame.display.flip() #perbarui display
        pygame.time.Clock().tick(60) #FPS = 60
    
    
import pygame
import sys
import time
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
        #dapatkan nilai koordinat x dan y maksimum (nilai mutlak)
        #bertujuan untuk scaling
        xMax,yMax = getMaximumCoordinates(ControlPointList)
        #bagi sumbu x menjadi 10 ke atas dan 10 ke bawah
        #10 ke bawah
        divisorY = newOrigin.y
        divisorValue = 0
        for i in range(11):
            divisorY += (screenHeight//22)
            divisorValue -= (yMax / 10)
            pygame.draw.line(screen,BLACK,(0,divisorY),(screenWidth,divisorY),1)
            ySurface = font.render(f"{divisorValue:.2f}", True, BLACK) 
            yRect = ySurface.get_rect()
            yRect.topleft = (newOrigin.x + 10, divisorY) 
            screen.blit(ySurface, yRect)
            
            
        #10 ke atas
        divisorY = newOrigin.y
        divisorValue = 0
        for i in range(11):
            divisorValue += (yMax / 10)
            divisorY -= (screenHeight//20-5)
            pygame.draw.line(screen,BLACK,(0,divisorY),(screenWidth,divisorY),1)
            ySurface = font.render(f"{divisorValue:.2f}", True, BLACK) 
            yRect = ySurface.get_rect()
            yRect.topleft = (newOrigin.x - 30, divisorY) 
            screen.blit(ySurface, yRect)
        #10 ke kanan
        divisorX = newOrigin.x
        divisorValue = 0
        for i in range(11):
            divisorX += (screenWidth//22)
            divisorValue += (xMax / 10)
            pygame.draw.line(screen,BLACK,(divisorX,0),(divisorX,screenHeight),1)
            xSurface = font.render(f"{divisorValue:.2f}", True, BLACK) 
            XRect = xSurface.get_rect()
            XRect.topleft = (divisorX, newOrigin.y + 10) 
            screen.blit(xSurface, XRect)
        #10 ke kiri
        divisorX = newOrigin.x
        divisorValue = 0
        for i in range(11):
            divisorX -= (screenWidth//22)
            divisorValue -= (xMax / 10)
            pygame.draw.line(screen,BLACK,(divisorX,0),(divisorX,screenHeight),1)
            xSurface = font.render(f"{divisorValue:.2f}", True, BLACK) 
            XRect = xSurface.get_rect()
            XRect.topleft = (divisorX, newOrigin.y - 20) 
            screen.blit(xSurface, XRect)
        pygame.display.flip() #tampilkan koordinat kartesius
        #perbarui yMax dan xMax untuk scaling
        xMax += (xMax/10)
        yMax += (yMax/10)
        #gambar semua control point di pygame
        scaledControlPointList = []
        for i in ControlPointList:
            scaledPoint = scaleToScreen(i,screenWidth,screenHeight,xMax,yMax) #rescale agar sesuai dengan layar di pygame
            scaledPoint = Point(scaledPoint.x,scaledPoint.y- 2 * abs(newOrigin.y - scaledPoint.y),i.pointName) #balik posisi y karena koordinat sumbu y di pygame terbalik
            scaledControlPointList.append(scaledPoint)
            pygame.draw.circle(screen,BLUE,(scaledPoint.x,scaledPoint.y),10) #gambar control point (titik warna biru) (y dibalik karena pygame koordinat y positif arahnya ke bawah)

            text_surface = font.render(f"{i.pointName} ({i.x}, {i.y})", True, BLACK) 
            text_rect = text_surface.get_rect()
            text_rect.topleft = (scaledPoint.x + 10, scaledPoint.y - 20)  # Position the text near the point (y dibalik karena di pygame koordinat y positif arahnya ke bawah)
            screen.blit(text_surface, text_rect)

            pygame.time.wait(1000) #delay 1 detik
            pygame.display.flip() #perbarui titik
        pygame.time.wait(2000) #delay 5 detik
        pygame.display.flip() #perbarui display
        #gambar garis di antara control point
        for i in range(0,len(scaledControlPointList)-1):
            drawLineAtoB(scaledControlPointList[i],scaledControlPointList[i+1],screen,BLUE)

        pygame.time.wait(2000) #delay 3 detik
        pygame.display.flip() #perbarui display
        pygame.time.Clock().tick(60) #FPS = 60

def getMaximumCoordinates(ControlPointList):
    retX = -9999999999999999999999999999999
    retY = -9999999999999999999999999999999

    for i in ControlPointList:
        if(abs(i.x) > retX):
            retX = abs(i.x)
        if(abs(i.y)> retY):
            retY = abs(i.y)

    return retX,retY

def scaleToScreen(P : Point, screenWidth, screenHeight, xMax, yMax) -> Point:
    xMin = -xMax
    yMin = -yMax

    scaledX = ((P.x - xMin) / (xMax-xMin)) * screenWidth
    scaledY = ((P.y - yMin) / (yMax-yMin)) * screenHeight

    scaledPoint = Point(scaledX,scaledY,P.pointName)
    return scaledPoint

def drawLineAtoB(A:Point, B:Point, screen, color):
    pygame.draw.line(screen,color,(A.x,A.y),(B.x,B.y),3)
    pygame.time.wait(1000)
    pygame.display.flip()

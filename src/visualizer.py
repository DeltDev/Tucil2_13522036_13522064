import pygame
import sys
from point import Point
from helper import getSRCDir
def spawnPygame(ControlPointList,BezierPointList,MidpointList,BezierMethod):
    #inisialisasi pygame
    pygame.init()
    pygame.display.set_caption('Visualizer Kurva Bezier')
    Icon = pygame.image.load(getSRCDir()+'\BezierCurveIcon.png')
    pygame.display.set_icon(Icon)
    font = pygame.font.Font(None,20)
    font2 = pygame.font.Font(None,35)
    #Warna
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    PUREBLACK = (0,0,0)
    BLACK = (75, 79, 76)
    BGCOLOR = (168, 167, 157)

    #setup ukuran layar
    screenWidth = 1280
    screenHeight = 720
    screen = pygame.display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)

    #buat origin baru karena titik origin pertama di pygame di pojok kiri atas
    newOrigin = Point(screenWidth//2,screenHeight//2,"Origin")
    #loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        #Update state pygame
                
        screen.fill(BGCOLOR) #warnai background
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
            divisorY -= (screenHeight//22)
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
            scaledPoint = Point(scaledPoint.x,scaledPoint.y,i.pointName)
            scaledControlPointList.append(scaledPoint)
            pygame.draw.circle(screen,BLUE,(scaledPoint.x,scaledPoint.y),10) #gambar control point (titik warna biru) (y dibalik karena pygame koordinat y positif arahnya ke bawah)

            text_surface = font.render(f"{i.pointName} ({i.x}, {i.y})", True, PUREBLACK) 
            text_rect = text_surface.get_rect()
            text_rect.topleft = (scaledPoint.x-50, scaledPoint.y + 20)  # Position the text near the point (y dibalik karena di pygame koordinat y positif arahnya ke bawah)
            screen.blit(text_surface, text_rect)

            pygame.time.wait(1000) #delay 1 detik
            pygame.display.flip() #perbarui titik
        pygame.time.wait(2000) #delay 5 detik
        pygame.display.flip() #perbarui display
        #gambar garis di antara control point
        for i in range(0,len(scaledControlPointList)-1):
            drawLineAtoB(scaledControlPointList[i],scaledControlPointList[i+1],screen,BLUE,1000)
        pygame.time.wait(2000) #delay 2 detik
        pygame.display.flip() #perbarui display

        
        scaledBezierPointList = []
        scaledMidpointList = []

        if(BezierMethod == "Brute Force"):#gambar titik bezier (brute force)
            # print("Memvisualisasikan Kurva Bezier dengan Brute Force")
            for i in BezierPointList:
                scaledPoint = scaleToScreen(i,screenWidth,screenHeight,xMax,yMax) #rescale agar sesuai dengan layar di pygame
                scaledPoint = Point(scaledPoint.x,scaledPoint.y,i.pointName)
                scaledBezierPointList.append(scaledPoint)
                pygame.draw.circle(screen,RED,(scaledPoint.x,scaledPoint.y),3) #gambar titik di kurva bezier (merah)
                pygame.time.wait(500) #delay 0.5 detik
                pygame.display.flip() #perbarui titik
            pygame.time.wait(2000) #delay 2 detik
            pygame.display.flip() #perbarui display
            #gambar kurva bezier (brute force)
            for i in range(0,len(scaledBezierPointList)-1):
                drawLineAtoB(scaledBezierPointList[i],scaledBezierPointList[i+1],screen,RED,500)
        elif(BezierMethod == "Divide And Conquer"): #gambar midpoint dan kurva bezier (divide and conquer)
            #gambar semua mid point
            for i in MidpointList:
                scaledPoint = scaleToScreen(i,screenWidth,screenHeight,xMax,yMax) #rescale agar sesuai dengan layar di pygame
                scaledPoint = Point(scaledPoint.x,scaledPoint.y,i.pointName)
                scaledMidpointList.append(scaledPoint)
                pygame.draw.circle(screen,GREEN,(scaledPoint.x,scaledPoint.y),3) #gambar midpoint (hijau)
                pygame.time.wait(500) #delay 0.5 detik
                pygame.display.flip() #perbarui titik
            pygame.time.wait(2000) #delay 2 detik
            pygame.display.flip() #perbarui display
            #gambar garis di antara midpoint
            for i in range(0,len(scaledMidpointList)):
                if(scaledMidpointList[i].pointName == "KIRI" or scaledMidpointList[i].pointName == "TENGAH"): #hanya gambar garis yang diberi nama "KIRI"
                    drawLineAtoB(scaledMidpointList[i],scaledMidpointList[i+1],screen,GREEN,500)

            for i in BezierPointList:
                scaledPoint = scaleToScreen(i,screenWidth,screenHeight,xMax,yMax) #rescale agar sesuai dengan layar di pygame
                scaledPoint = Point(scaledPoint.x,scaledPoint.y,i.pointName)
                scaledBezierPointList.append(scaledPoint)
                pygame.draw.circle(screen,RED,(scaledPoint.x,scaledPoint.y),3) #gambar titik di kurva bezier (merah)
                pygame.time.wait(500) #delay 0.5 detik
                pygame.display.flip() #perbarui titik
            pygame.time.wait(2000) #delay 2 detik
            pygame.display.flip() #perbarui display
            #gambar kurva bezier (brute force)
            for i in range(0,len(scaledBezierPointList)-1):
                drawLineAtoB(scaledBezierPointList[i],scaledBezierPointList[i+1],screen,RED,500)

        pygame.time.wait(10000) #delay 10 detik untuk memberikan kesempatan kepada pengguna untuk menekan tombol exit
        pygame.display.flip() #perbarui display
        pygame.time.Clock().tick(60) #FPS = 60

def getMaximumCoordinates(ControlPointList): #fungsi untuk mendapatkan nilai x dan y maksimum
    retX = -9999999999999999999999999999999
    retY = -9999999999999999999999999999999

    for i in ControlPointList:
        if(abs(i.x) > retX):
            retX = abs(i.x)
        if(abs(i.y)> retY):
            retY = abs(i.y)

    return retX,retY

def scaleToScreen(P : Point, screenWidth, screenHeight, xMax, yMax) -> Point: #fungsi untuk rescale titik ke layar pygame
    xMin = -xMax
    yMin = -yMax

    scaledX = ((P.x - xMin) / (xMax-xMin)) * screenWidth
    scaledY = ((P.y - yMin) / (yMax-yMin)) * screenHeight

    scaledPoint = Point(scaledX,screenHeight-scaledY,P.pointName) #balik nilai y karena di pygame koordinatnya terbalik
    return scaledPoint

def drawLineAtoB(A:Point, B:Point, screen, color,duration): #prosedur untuk menggambar garis dari titik A ke titik B dengan durasi dan warna yang ditentukan
    pygame.draw.line(screen,color,(A.x,A.y),(B.x,B.y),3)
    pygame.time.wait(duration)
    pygame.display.flip()

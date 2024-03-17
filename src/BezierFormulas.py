from point import Point
def LinearBezier(ControlPoint0: Point, ControlPoint1 : Point, t: int) -> Point: #Persaman kurva Bezier Linear
    Pt = Point((ControlPoint0.x + t * (ControlPoint1.x - ControlPoint0.x)), (ControlPoint0.y + t * (ControlPoint1.y - ControlPoint0.y)), "")
    return Pt

def QuadraticBezier(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, t: int) -> Point: #Persamaan kurva Bezier Kuadratik
    Q1 = LinearBezier(ControlPoint0, ControlPoint1, t)
    Q2 = LinearBezier(ControlPoint1, ControlPoint2, t)
    R = LinearBezier(Q1,Q2,t)
    return R

# kalau jadi kerjain bonus satu
def Combination(n: int, r: int) -> int:
    C = 1
    for i in range(n, r, -1): C *= i
    for i in range(2, (n - r + 1)): C //= i
    return C

# untuk brute force
def UltimateBezierFormula(ControlPointsList : list[Point], t : float) -> Point: # sesuai dengan panjang list ControlPointsList
    order = len(ControlPointsList) - 1
    X = Point(0, 0, "NEW")
    for i in range (order + 1):
        X.x += Combination(order, i) * ((1 - t) ** (order - i)) * (t ** i) * ControlPointsList[i].x
        X.y += Combination(order, i) * ((1 - t) ** (order - i)) * (t ** i) * ControlPointsList[i].y
    return X

# algo brute force
def BruteForceBezier(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, iteration: int) -> list[Point]:
    # termasuk titik ujungnya
    return [QuadraticBezier(ControlPoint0, ControlPoint1, ControlPoint2, n/iteration) for n in range (iteration + 1)]

# divide and conquer
def DivideAndConquerBezier(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, iteration: int,MidpointArray):
    if(iteration > 0): #selama iterasinya belum mencapai 0
        Midpoint1 = Midpoint(ControlPoint0,ControlPoint1,"KIRI") #cari titik tengah di antara garis di control point 0 dan control point 1
        Midpoint2 = Midpoint(ControlPoint1,ControlPoint2,"KANAN") #cari titik tengah di antara garis di control point 1 dan control point 2
        ExtraPoint = Midpoint(Midpoint1,Midpoint2,"TENGAH") #cari titik tengah di antara garis di midpoint 1 dan midpoint 2 (titik di kurva bezier)
        #urutannya akan selalu "KIRI","KANAN","TENGAH". yang akan membentuk garis di visualisasi hanyalah titik yang diberi nama "KIRI"
        #yang akan dianggap titik di kurva bezier adalah titik yang diberi nama "TENGAH"
        MidpointArray.append(Midpoint1)
        MidpointArray.append(Midpoint2)
        DivideAndConquerBezier(ControlPoint0,Midpoint1,ExtraPoint,iteration-1,MidpointArray) #divide permasalahan ke kiri
        MidpointArray.append(ExtraPoint)
        DivideAndConquerBezier(ExtraPoint,Midpoint2,ControlPoint2,iteration-1,MidpointArray) #divide permasalahan ke kanan

def UltimateBezierBattle(ControlPointsList : list[Point], iteration: int, MidpointArray):
    if(iteration > 0): #selama iterasinya belum mencapai 0
        order = len(ControlPointsList) - 1
        NewLeft = [ControlPointsList[0]]
        NewRight = [ControlPointsList[order]]
        ExtraPoint = Point(0, 0, "NEW")
        for i in range (order, 0, -1):
            if (i == 1):
                if ((order + 1) == 2): # jaga jaga kalau tiba tiba masukan pointnya cuma dua. Kalau merasa tidak perlu hapus kondisi ini (langsung ke else dibawahnya)
                    ExtraPoint = Midpoint(ControlPointsList[0], ControlPointsList[1], "NEW")
                else:
                    ExtraPoint = Midpoint(MidpointArray[len(MidpointArray) - 2], MidpointArray[len(MidpointArray) - 1], "NEW")
                NewLeft.append(ExtraPoint)
                NewRight = [ExtraPoint] + NewRight
            elif (i == order):
                for j in range (i):
                    if (j == 0):
                        NewPoint = Midpoint(ControlPointsList[j], ControlPointsList[j + 1], "KIRI")
                        NewLeft.append(NewPoint)
                    elif (j == (i - 1)):
                        NewPoint = Midpoint(ControlPointsList[j], ControlPointsList[j + 1], "KANAN")
                        NewRight = [NewPoint] + NewRight
                    else:
                        NewPoint = Midpoint(ControlPointsList[j], ControlPointsList[j + 1], "TENGAH")
                    MidpointArray.append(NewPoint)
            else:
                for j in range (i):
                    if (j == 0):
                        NewPoint = Midpoint(MidpointArray[len(MidpointArray) - i - 1], MidpointArray[len(MidpointArray) - i], "KIRI")
                        NewLeft.append(NewPoint)
                    elif (j == (i - 1)):
                        NewPoint = Midpoint(MidpointArray[len(MidpointArray) - i - 1], MidpointArray[len(MidpointArray) - i], "KANAN")
                        NewRight = [NewPoint] + NewRight
                    else:
                        NewPoint = Midpoint(MidpointArray[len(MidpointArray) - i - 1], MidpointArray[len(MidpointArray) - i], "TENGAH")
                    MidpointArray.append(NewPoint)
        UltimateBezierBattle(NewLeft,iteration-1,MidpointArray) #divide permasalahan ke kiri
        MidpointArray.append(ExtraPoint)
        UltimateBezierBattle(NewRight,iteration-1,MidpointArray) #divide permasalahan ke kanan
    return
    
def Midpoint(ControlPoint1, ControlPoint2, MidpointName): #hitung Midpoint dan namanya (nama bertujuan untuk membedakan midpoint di visualisasi nanti)
    newMidpoint = Point((ControlPoint1.x + ControlPoint2.x) / 2, (ControlPoint1.y + ControlPoint2.y) / 2, MidpointName)
    return newMidpoint

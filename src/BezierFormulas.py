from point import Point
def LinearBezier(ControlPoint0: Point, ControlPoint1 : Point, t: int) -> Point: #Persaman kurva Bezier Linear
    Pt = Point((ControlPoint0.x + t * (ControlPoint1.x - ControlPoint0.x)), (ControlPoint0.y + t * (ControlPoint1.y - ControlPoint0.y)))
    return Pt

def QuadraticBezier(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, t: int) -> Point: #Persamaan kurva Bezier Kuadratik
    Q1 = LinearBezier(ControlPoint0, ControlPoint1, t)
    Q2 = LinearBezier(ControlPoint1, ControlPoint2, t)
    R = LinearBezier(Q1,Q2,t)
    return R

# kalau jadi kerjain bonus satu
"""def Combination(n: int, r: int) -> int:
    C = 1
    for i in range(n, r, -1): C *= i
    for i in range(2, (n - r + 1)): C //= i
    return C

# untuk brute force
def UltimateBezierFormula(ControlPointsList : list[Point], t : float) -> Point: # sesuai dengan panjang list ControlPointsList
    order = len(ControlPointsList) - 1
    X = Point(0, 0)
    for i in range (order + 1):
        X.x += Combination(order, i) * ((1 - t) ** (order - i)) * (t ** i) * ControlPointsList[i].x
        X.y += Combination(order, i) * ((1 - t) ** (order - i)) * (t ** i) * ControlPointsList[i].y
    return X"""

# algo brute force
def BruteForceBezier(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, iteration: int) -> list[Point]:
    # termasuk titik ujungnya
    return [QuadraticBezier(ControlPoint0, ControlPoint1, ControlPoint2, n/iteration) for n in range (iteration + 1)]

# divide and conquer

# gak yakin gimana untuk bonus2nya kalau butuh extra info untuk visualizer
"""def DivideAndConquerBezierWithExtraSteps(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, iteration: int) -> list[list[list[Point]]]:
    Midpoint1 = Point((ControlPoint0.x + ControlPoint1.x) / 2, (ControlPoint0.y + ControlPoint1.y) / 2)
    Midpoint2 = Point((ControlPoint1.x + ControlPoint2.x) / 2, (ControlPoint1.y + ControlPoint2.y) / 2)
    ExtraPoint = Point((Midpoint1.x + Midpoint2.x) / 2, (Midpoint1.y + Midpoint2.y) / 2)
    if (iteration == 1):
        return [[[ControlPoint0, ControlPoint1, ControlPoint2, Midpoint1, Midpoint2, ExtraPoint]]]
    else:
        Left = DivideAndConquerBezierWithExtraSteps(ControlPoint0, Midpoint1, ExtraPoint, iteration - 1)
        Right = DivideAndConquerBezierWithExtraSteps(ExtraPoint, Midpoint2, ControlPoint2, iteration - 1)
        E = [[[ControlPoint0, ControlPoint1, ControlPoint2, Midpoint1, Midpoint2, ExtraPoint]]] + [(Left[i] + Right[i]) for i in range (len(Left))]
        return E"""

# bare minimum version
def DivideAndConquerBezier(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, iteration: int) -> list[Point]:
    Midpoint1 = Point((ControlPoint0.x + ControlPoint1.x) / 2, (ControlPoint0.y + ControlPoint1.y) / 2)
    Midpoint2 = Point((ControlPoint1.x + ControlPoint2.x) / 2, (ControlPoint1.y + ControlPoint2.y) / 2)
    ExtraPoint = Point((Midpoint1.x + Midpoint2.x) / 2, (Midpoint1.y + Midpoint2.y) / 2)
    if (iteration == 1):
        return [ControlPoint0, ExtraPoint, ControlPoint2]
    else:
        Left = DivideAndConquerBezier(ControlPoint0, Midpoint1, ExtraPoint, iteration - 1)
        Right = DivideAndConquerBezier(ExtraPoint, Midpoint2, ControlPoint2, iteration - 1)
        Left.pop()
        return (Left + Right)

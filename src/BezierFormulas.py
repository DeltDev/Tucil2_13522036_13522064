from point import Point
def LinearBezier(ControlPoint0: Point, ControlPoint1 : Point, t: int) -> Point: #Persaman kurva Bezier Linear
    Pt = Point((ControlPoint0.x + t * (ControlPoint1.x - ControlPoint0.x)), (ControlPoint0.y + t * (ControlPoint1.y - ControlPoint0.y)))
    return Pt

def QuadraticBezier(ControlPoint0 : Point, ControlPoint1: Point, ControlPoint2: Point, t: int) -> Point: #Persamaan kurva Bezier Kuadratik
    Q1 = LinearBezier(ControlPoint0, ControlPoint1, t)
    Q2 = LinearBezier(ControlPoint1, ControlPoint2, t)
    R = LinearBezier(Q1,Q2,t)
    return R
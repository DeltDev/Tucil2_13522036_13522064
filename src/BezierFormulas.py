from point import Point
def LinearBezier(ControlPoint0: Point, ControlPoint1 : Point, t: int) -> Point: #Persaman kurva Bezier Linear
    Pt = Point((ControlPoint0.x + t * (ControlPoint1.x - ControlPoint0.x)), (ControlPoint0.y + t * (ControlPoint1.y - ControlPoint0.y)))
    return Pt


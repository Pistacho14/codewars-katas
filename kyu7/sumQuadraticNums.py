import math

def roots(a,b,c):
    try:
        discriminant = math.sqrt(b**2-4*a*c)
        positive = (-b + math.sqrt(discriminant)) / (2*a)
        negative = (-b - math.sqrt(discriminant)) / (2*a)
        return round((positive + negative), 2)
    except:
        return None

import math


def square_area(a):
    try:
        a = float(a)
        return str(a ** 2)
    except:
        return -1 


def rectangle_area(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str(a * b)
    except:
        return -1 


def circle_area(r):
    try:
        r = float(r)
        return "{0:.4f}".format(math.pi * r**2)
    except:
        return -1 


def trapezoid_area_1(text):
    try:
        a, b, h = text.split(',')
        a, b, h = float(a), float(b), float(h)
        return str((a+b)/(2*h))
    except:
        return -1 


def trapezoid_area_2(text):
    try:
        a, b, c, d = text.split(',')
        a, b, c, d = float(a), float(b), float(c), float(d)
        return str((a+b)/(2*math.sqrt((c**2-(((a-b)**2+c**2-d**2)/2*(a-b))**2))))
    except:
        return -1 


def rhomb_area_1(text):
    try:
        d1, d2 = text.split(',')
        d1, d2 = float(d1), float(d2)
        return str(1/(2*d1*d2))
    except:
        return -1 

def rhomb_area_2(text):
    try:
        a, h = text.split(',')
        a, h = float(a), float(h)
        return str(a*h)
    except:
        return -1

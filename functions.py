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
        return "{0:.4f}".format(math.pi * r ** 2)
    except:
        return -1


def trapezoid_area_1(text):
    try:
        a, b, h = text.split(',')
        a, b, h = float(a), float(b), float(h)
        return str((a + b) / (2 * h))
    except:
        return -1


def trapezoid_area_2(text):
    try:
        a, b, c, d = text.split(',')
        a, b, c, d = float(a), float(b), float(c), float(d)
        return str((a + b) / 2 * (math.sqrt((c ** 2 - (((a - b) ** 2 + c ** 2 - d ** 2) / 2 * (a - b)) ** 2))))
    except:
        return -1


def pyramid_area(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str(a ** 2 + (2 * a) * (math.sqrt(b ** 2 - (a ** 2 / 4))))
    except:
        return -1


def area_of_a_right_triangle(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str(0.5 * a * b)
    except:
        return -1


def parallelogram_area(text):
    try:
        a, h = text.split(',')
        a, h = float(a), float(h)
        return str(a * h)
    except:
        return -1


def cylinder_area(text):
    try:
        r, h = text.split(',')
        r, h = float(r), float(h)
        return str(2*math.pi*r*(h+r))
    except:
        return -1


def area_of_the_cone(text):
    try:
        r, l = text.split(',')
        r, l = float(r), float(l)
        return str(math.pi * r * l + math.pi * (r ** 2))
    except:
        return -1


def rhomb_area_1(text):
    try:
        d1, d2 = text.split(',')
        d1, d2 = float(d1), float(d2)
        return str(0.5 * d1 * d2)
    except:
        return -1


def rhomb_area_2(text):
    try:
        a, h = text.split(',')
        a, h = float(a), float(h)
        return str(a * h)
    except:
        return -1


def exponentiation(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str(a ** b)
    except:
        return -1


def logarithm(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str(math.log(a, b))
    except:
        return -1


def root_extraction(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str()
    except:
        return -1


def greatest_common_divisor(text):
    try:
        a, b = text.split(',')
        a, b = int(a), int(b)
        return str(math.gcd(a, b))
    except:
        return -1


def nok(text):
    try:
        a, b = text.split(',')
        a, b = int(a), int(b)
        return str((a*b)/(math.gcd(a, b)))
    except:
        return -1


def factorial(a):
    try:
        a = int(a)
        return str(math.factorial(a))
    except:
        return -1


def percent_1(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str((a/b)*100) + '%'
    except:
        return -1


def percent_2(text):
    try:
        a, b = text.split(',')
        a, b = float(a), float(b)
        return str((a/100)*b)
    except:
        return -1

import math
import sys
from math import sqrt, sin, pi
import sympy

def isNumber(number):
    try:
        float(number)
        return True
    except:
        return False

def theorem_seq_sort(t):
    if 24 <= t <= 28:
        return 10
    if t == 19:
        return 20
    if t == 1:
        return 20
    if t >= 29:
        return 100
    return 50

def logic_forms_sort(s):
    if "Perpendicular" in s:
        return 50
    elif "Equals" in s:
        return 100
    elif "Parallel" in s:
        return 10
    elif "Tangent" in s:
        return 40
    elif "PointLiesOnLine" in s:
        return 1
    elif "PointLiesOnCircle" in s:
        return 2
    else:
        return 5
    
def hasNumber(lst):
    for number in lst:
        try:
            float(number)
            return True
        except:
            pass
    return False

def isAlgebra(number):
    if isNumber(number):
        return True
    if isinstance(number, sympy.Basic) and '_' not in str(number) and 'angle' not in str(number):
        return True
    else:
        return False
    
def findAlgebra(lst):
    for number in lst:
        if isAlgebra(number):
            return number
    return None

def sort_angle(angle):
    assert len(angle) == 3
    if angle[0] > angle[2]: return angle[::-1]
    return angle

def sort_points(points):
    min_index = points.index(min(points))
    if points[(min_index-1+len(points))%len(points)] > points[(min_index+1)%len(points)]:
        sorted_points = points[min_index:] + points[:min_index]
    else:
        sorted_points = points[min_index::-1] + points[:min_index:-1]
    return sorted_points

# Note: We should calculate the value explicitly, so use math.xxx not sympy.xxx

def heron_triangle_formula(a,b,c):
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

def angle_area_formula(a,b, angle):
    return 0.5 * a * b * sin(pi / 180.0 * angle)

def cos_law_length():
    pass

def cos_law_angle():
    pass

def sin_law_length():
    pass

def sin_law_angle():
    pass

if __name__ == '__main__':
    area = heron_triangle_formula(3,4,5)
    assert area == 6.0
    area = angle_area_formula(3,4,90)
    assert area == 6.0



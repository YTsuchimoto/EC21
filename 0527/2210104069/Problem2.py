# Problem 2
from math import sqrt, sin, cos, pi

# Initialize points at T = 0
O = [0, 0] 
A = [2, 0]
P1 = [5, 0]
P2 = [10, 0]

# Return coordinates of the rotated point regarding the parameter "angle"
def rotate(point, angle):
    rotated_point = [point[0]*cos(angle) - point[1]*sin(angle), point[1]*sin(angle) + point[0]*sin(angle)]
    return rotated_point

# Return the area of the triangle composed by A, P1 and P2 regarding their rotation around O
def triangleArea(A, newP1, newP2):
    x1, y1, x2, y2, x3, y3 = A[0], A[1], newP1[0], newP1[1], newP2[0], newP2[1]
    return abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1))))

# Return the maximum value of the area ΔA,P1,P2
def findMaxArea(A, P1, P2, step):
    max_area = triangleArea(A, P1, P2)
    for i in range(0, step):
        angle = i*2*pi/step
        newP1 = rotate(P1, 2*angle)
        newP2 = rotate(P2, angle)
        new_area = triangleArea(A, newP1, newP2)
        if new_area > max_area:
            max_area = new_area
    return max_area

step = 1*10**5
print("Max value of the area is : ", findMaxArea(A, P1, P2, step))
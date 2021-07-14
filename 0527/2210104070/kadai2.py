import sympy
from sympy import sin, cos

def main():
    theta = sympy.Symbol('theta',real='True')
    a_x = 2
    a_y = 0
    p1_x = 5*cos(2*theta)
    p1_y = 5*sin(2*theta)
    p2_x = 10*cos(theta)
    p2_y = 10*sin(theta)
    S = sympy.trigsimp((1 / 2) * ((p1_x - a_x) * (p2_y - a_y) - (p2_x - a_x) * (p1_y - a_y)))
    grad_S = sympy.diff(S,theta)
    theta_candidate = sympy.solve(grad_S)
    S_candidate = []
    for i in theta_candidate:
        S_candidate.append(S.subs(theta,i))
    
    print(max(S_candidate))

if __name__ == '__main__':
    main()
import sympy
from sympy import sin, cos


def main():
    '''Answer
    max: 36.3092188706945
    '''

    theta = sympy.Symbol('theta', real=True)
    a_x = 2
    a_y = 0
    p1_x = 5 * cos(2 * theta)
    p1_y = 5 * sin(2 * theta)
    p2_x = 10 * cos(theta)
    p2_y = 10 * sin(theta)

    # note: S is not non-negative
    S = sympy.trigsimp(
        (1 / 2) * ((p1_x - a_x) * (p2_y - a_y) - (p2_x - a_x) * (p1_y - a_y))
    )
    '''
    S = sympy.trigsimp(
        (1 / 2) * ((p2_x - a_x) * (p1_y - a_y) - (p1_x - a_x) * (p2_y - a_y))
    )
    '''

    grad_S = sympy.diff(S, theta)
    theta_extremum = sympy.solve(grad_S)
    S_extremum = []
    for t in theta_extremum:
        S_extremum.append(S.subs(theta, t))

    print(theta_extremum)
    print(S_extremum)
    print(max(S_extremum))


if __name__ == '__main__':
    main()

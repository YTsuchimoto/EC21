from sympy import *

def main():
    theta = Symbol('theta')

    ax = 2
    ay = 0

    p1x = 5 * cos(2 * theta)
    p1y = 5 * sin(2 * theta)
    p2x = 10 * cos(theta)
    p2y = 10 * sin(theta)

    area = ((p1x-ax)*(p2y-ay)-(p2x-ax)*(p1y-ay)) / 2
    area = trigsimp(area)
    # print(area)
    diff_area = area.diff(theta)
    # print(diff_area)
    results = solve(diff_area)
    # print(results)

    answers = []
    for result in results:
        answer = area.subs(theta, result)
        answers.append(abs(answer))

    print(trigsimp(max(answers)))

if __name__ == '__main__':
    main()
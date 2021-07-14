def primes_list(x):
    if x < 2 : return []
    prims = [2]
    for i in range(3,x) :
        if all((i % p != 0 for p in prims)) :
            prims.append(i)
    return prims

def slv(xs):
    S_A = []
    S_B = []
    for x in reversed(xs):
      if sum(S_A) - sum(S_B) > 0:
          S_B.append(x)
      else :
          S_A.append(x)
    return S_A, S_B

def thn():
    import numpy as np
    import theano.tensor as T
    from theano import function, shared
    eps = 10e-5
    learning_rate = 10e-3
    max_num = 100000

    theta = T.dscalar('theta')
    S = 35 * np.sin(theta) - 5 * np.sin(2 * theta)

    gS = T.grad(cost=S, wrt=theta)
    x = shared(value=2*np.pi*np.random.rand(), name='x')

    f_S = function(inputs=[theta], outputs=abs(S))
    f_gS = function(inputs=[theta], outputs=gS)
    grad_descent = function(inputs=[theta], outputs=gS, updates=[(x, x - learning_rate * gS)])
    for i in range(max_num):
        grad_descent(x.get_value())

        if abs(f_gS(x.get_value())) <= eps:
            break

    return f_S(x.get_value())

def sym():
    from sympy import Symbol, geometry, cos, sin, solve, diff
    theta = Symbol('theta', real=True)
    vtxes = geometry.Polygon((2, 0), (5 * cos(2 * theta), 5 * sin(2 * theta)), (10 * cos(theta), 10 * sin(theta)))

    S_max = 0
    for x in solve(diff(vtxes.area, theta)) :
        S = vtxes.area.subs(theta, x)
        if S_max < S :
          S_max = S
    return float(S_max)

if __name__ == '__main__':
    ps = primes_list(100)
    S_A, S_B = slv(ps)
    print(sum(S_A))
    print(S_A)
    print(sum(S_B))
    print(S_B)
    print('theano : max_S = {}'.format(thn()))
    print('sympy : max_S = {}'.format(sym()))

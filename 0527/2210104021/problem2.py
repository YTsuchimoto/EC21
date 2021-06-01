# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:04:32 2021

@author: kkawa
"""

import sympy

def main():
    theta = sympy.Symbol('theta')
    
    S = 25 * sympy.sin(theta / 2)
    
    fd = sympy.diff(S)
    
    sol_fd = sympy.solve(fd, theta)
    
    ex_value = list(map(lambda x : S.subs(theta, x), sol_fd))

    print("最大値 : " + str(max(ex_value)))
    
if __name__ == "__main__":
    main()
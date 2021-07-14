#Ryuhei Nishida
#2210104058

# -*- coding: utf-8 -*-
import numpy as np
from sympy import *
def main():
    x = Symbol("x",real=True)
    

    f=((5*cos(2*x)*10*sin(x))-5*sin(2*x)*(10*cos(x)-2))/2
    f=simplify((f))
    f_d =diff(f,x)

    xd = solve(f_d,x)
    if(f.subs(x,xd[0])>f.subs(x,xd[1])):
        print("最大値:"+str(f.subs(x,xd[0])))
    else:
        print("最大値:"+str(f.subs(x,xd[1])))

if __name__ == '__main__':
    main()
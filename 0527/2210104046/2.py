import sympy

XofA = 2
YofA = 0
theta = sympy.Symbol('theta',real='True')

XofP1 = 5*sympy.cos(2*theta)
YofP1 = 5*sympy.sin(2*theta)
XofP2 = 10*sympy.cos(theta)
YofP2 = 10*sympy.sin(theta)

S = sympy.trigsimp((1/2)*((XofP1-XofA)*(YofP2-YofA)-(XofP2-XofA)*(YofP1-YofA)))
dif = sympy.diff(S,theta)
AllofTheta = sympy.solve(dif)
print("Theta:",AllofTheta,"\n")

AllofS = []

for i in AllofTheta:
    AllofS.append(S.subs(theta,i))
print("S:",AllofS,"\n")
    
print("Maximum:",max(AllofS),"\n")


    



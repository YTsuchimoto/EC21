import math

ax=2
ay=0

w=0.000001
t=0
sb=0
while w*t < 2*math.pi:
	p1x=5*math.cos(w*t)
	p1y=5*math.sin(w*t)
	p2x=10*math.cos(2*w*t)
	p2y=10*math.sin(2*w*t)
	
	s=abs((ax-p2x)*(p1y-p2y)-(p1x-p2x)*(ay-p2y))
	#print(s)
	if sb<s:
		sb=s
	t=t+1


print('最大面積'+str(sb))

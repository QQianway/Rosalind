import math 
import sys

A=19213	
B=16994
C=18978
D=19679
E=18373
F=17234

def dominantOff(A,B,C,D,E,F):
	a=A*2
	b=B*2
	c=C*2
	d=D*2*0.75
	e=E*2*0.5
	f=F*2*0

	p=a+b+c+d+e+f
	return p

print(dominantOff(A,B,C,D,E,F))

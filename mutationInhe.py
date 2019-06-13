import sys
import math

x=30
y=15
z=22

def mutationOff(x,y,z):
	total = x+y+z
	twoRecess = (z/total) * ((z-1)/(total-1))
	twoHetero = (y/total) * ((y-1)/(total-1))
	heteroRecess = ((y/total)*(z/(total-1)) + (z/total)*(y/(total-1)))
	p = 1 - twoRecess - twoHetero*0.25 - heteroRecess*0.5
	return p

print(mutationOff(x,y,z))

# def mendel(x, y, z):
#     #calculate the probability of recessive traits only
#     total = x+y+z
#     twoRecess = (z/total)*((z-1)/(total-1))
#     twoHetero = (y/total)*((y-1)/(total-1))
#     heteroRecess = (z/total)*(y/(total-1)) + (y/total)*(z/(total-1))

#     recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
#     return(1-recessProb) # take the complement
# print(mendel(x,y,z))

import sys

d={}
with open('dataset/MonoMass.txt','r')as fd:
	d=dict(line.strip().split(None,1) for line in fd)
	fd.close

proteinString = open('dataset/rosalind_prtm.txt').read()
mass=0

for letter in proteinString:
	for k,v in d.items():
		if k==letter:
			mass+=float(v)

print (round(mass,3))
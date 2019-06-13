import sys
import linecache

d=dict()
x=1

for x in range(1,200):
	line = linecache.getline('rosalind_ini6.txt',x)
	for word in line.split():
		if word in d:
			d[word] +=1
		else:
			d[word] =1

for key, value in d.items():
    print (key+" "+str(value))
import sys
import linecache

a=0
b=200


for x in range (a,b):
	if  x%2==0:
		line = linecache.getline('rosalind_ini5.txt', x)
		print(line)
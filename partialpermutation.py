import sys

def partial_permutation(a,b):
	i=0
	total=1
	while(i<b):
		total*=a
		b-=1
		a-=1
		print(total)
	result=total%1000000
	return result

small_dataset=(21,7)
large_dataset=open('dataset/rosalind_pper.txt').read().split()

a,b=large_dataset
a=int(a)
b=int(b)

print(partial_permutation(a,b))
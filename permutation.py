import itertools

large_dataset=open('dataset/rosalind_perm.txt').read()
large_dataset=int(large_dataset)
small_dataset=3


def permutation(n):
	total=1
	for i in range(1,n+1):
		total*=i
	print(total)
	permutation_list=list(itertools.permutations(range(1,n+1)))
	for x in permutation_list:
		for i in x:
			print(i,end=' ') 
		print('')


n=permutation(large_dataset)

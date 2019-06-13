from itertools import permutations, product

def merge_products(product):
	result= []
	numbers,signs=product
	for i,number in enumerate(numbers):
		sign=signs[i]
		number=int(sign+str(number))
		result.append(number)
	return result

def result(n):
	numbers=list(permutations(range(1,n+1)))
	signs= list(product('-+',repeat=n))

	results=list(product(numbers,signs))
	results=list(map(merge_products,results))
	return results

small_dataset=2
large_dataset=int(open('dataset/rosalind_sign.txt').read())
results=result(large_dataset)

print (len(results))
for r in results:
	print(' '.join(map(str,r)))
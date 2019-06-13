#independent alleles
from scipy.special import comb
large_dataset = open('dataset/rosalind_lia.txt').read()
large_dataset=large_dataset.split()
k=int(large_dataset[0])
n=int(large_dataset[1])
t = 2**k
print (round(sum([comb(t, i, 1) * 0.25**i * 0.75**(t-i) for i in range(n, t+1)]),3))

# from scipy.misc import comb
# k,n = 5,7
# t = 2**k
# print (round(sum([comb(t, i, 1) * 0.25**i * 0.75**(t-i) for i in range(n, t+1)]),3))
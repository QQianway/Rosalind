import math

def fasta(s):
    results={}
    string=s.strip().split('>')
    for s in string:
        if len(s)==0:
            continue
        part = s.split()
        result=[]
        for i in part:
            result.append(i)
    return result

AT = 0
GC = 0
large_dataset=open('dataset/rosalind_prob.txt').read()
large_dataset=fasta(large_dataset)
temp=large_dataset[0]
del large_dataset[0]
numbers=[]
for i in temp:
    if i == 'A' or i == 'T':
        AT += 1
    elif i == 'G' or i == 'C':
        GC += 1
numbers=[float(x) for x in large_dataset]

probabilities = []
for j in range(len(numbers)):
    prob = math.log10((((1 - numbers[j]) / 2)**AT) * (numbers[j] / 2)
                      **GC)
    probabilities.append('%0.3f' % prob)
print(*probabilities, sep=' ')
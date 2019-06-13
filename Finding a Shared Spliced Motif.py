#finding a shared spliced motif
#from Bio import SeqIO
def fasta(s):
    results={}
    string=s.strip().split('>')
    for s in string:
        if len(s)==0:
            continue
        part = s.split()
        label = part[0]
        bases = ''.join(part[1:])
        results[label] = bases
    return results
large_dataset = open('dataset/rosalind_lcsq.txt').read()
large_dataset=fasta(large_dataset)

temp=[]
for k,v in large_dataset.items():
    temp.append(v)
s,t=temp[0],temp[1] 

lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
#creates array of len(s) containing arrays of len(t) filled with 0
for i, x in enumerate(s):
    for j, y in enumerate(t):
        if x == y:
            lengths[i + 1][j + 1] = lengths[i][j] + 1
        else:
            lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

spliced_motif = ''
x, y = len(s), len(t)
while x * y != 0:
    if lengths[x][y] == lengths[x - 1][y]:
        x -= 1
    elif lengths[x][y] == lengths[x][y - 1]:
        y -= 1
    else:
        spliced_motif = s[x - 1] + spliced_motif
        x -= 1
        y -= 1
print(spliced_motif)
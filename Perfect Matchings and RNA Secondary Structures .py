from Bio import SeqIO                      
from math import factorial                                             

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

temp = ''                              
large_dataset = open('dataset/rosalind_pmch.txt').read()
large_dataset=fasta(large_dataset)
for k,v in large_dataset.items():
    temp=temp+v+'\n'           


AU = 0                                     
GC = 0                                     
for nt in temp:                        
    if nt == 'A':                          
        AU += 1                            
    elif nt == 'G':                        
        GC += 1                            

matchings = factorial(AU) * factorial(GC)  
print(matchings)


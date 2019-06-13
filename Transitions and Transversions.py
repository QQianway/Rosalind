#Transitions and Tranversions
from Bio import SeqIO               

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
large_dataset = open('dataset/rosalind_tran.txt').read()
large_dataset=fasta(large_dataset)

temp=[]
for k,v in large_dataset.items():
	temp.append(v)
s1,s2=temp[0],temp[1]                           

transition = 0                               
transversion = 0                             
AG = ['A', 'G']                              
CT = ['C', 'T']                              
for nt1, nt2 in zip(s1, s2):                 
    if nt1 != nt2:                           
        if nt1 in AG and nt2 in AG:          
            transition += 1                  
        elif nt1 in CT and nt2 in CT:        
            transition += 1                  
        else:                                
            transversion += 1                
print('%0.11f' % (transition / transversion))
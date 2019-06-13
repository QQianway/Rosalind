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

def revComplement( t ):
    rev = ''
    for c in t:
        if c == 'A':
            rev = 'T' + rev
        elif c == 'C':
            rev = 'G' + rev
        elif c == 'G':
            rev = 'C' + rev
        elif c == 'T':
            rev = 'A' + rev
    return rev

def isRevPalindrome( text ):
    return text == revComplement(text)

#define dna
dna = 'TCAATGCATGCGGGTCTATATGCAT'
large_dataset = open('dataset/rosalind_revp.txt').read()
large_dataset = fasta(large_dataset)
for k,v in large_dataset.items():
    for l in range(4,13):
        for i in range(0,len(v)-l+1):
            if isRevPalindrome(v[i:i+l]):
              print (str(i+1) + ' ' + str(l))
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

def subsequence_indices(s):
    indices = []

    s, t = s.split()

    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            indices.append(i + 1)
            # print(s[i]+t[j])
            j += 1
        i += 1

    return indices

small_dataset = "ACGTACGTGACG\nGTA"
large_dataset = open('dataset/rosalind_sseq.txt').read()
large_dataset=fasta(large_dataset)
temp=''
for k,v in large_dataset.items():
    temp=temp+v+'\n'
result = subsequence_indices(temp)
print (' '.join(map(str, result)))
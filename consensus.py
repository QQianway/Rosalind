import sys
from Bio import AlignIO


# def profile(matrix):
#     strings = matrix.split()
#     print
#     default = [0] * len(strings[0])
#     results = {
#         'A': default[:],
#         'C': default[:],
#         'G': default[:],
#         'T': default[:],
#     }
#     for s in strings:
#         for i, c in enumerate(s):
#             results[c][i] += 1
#     return results
def profile(matrix):
prof = [[0 for i in range(len(dna[0]))] for i in range(4)]
for seq in dna:
    for i in range(len(seq)):
        if seq[i] == 'A':
            prof[0][i] += 1
        elif seq[i] == 'C':
            prof[1][i] += 1
        elif seq[i] == 'G':
            prof[2][i] += 1
        elif seq[i] == 'T':
            prof[3][i] += 1
return prof


def consensus(profile):
    result = []

    keys = list(profile.keys())

    for i in range(len(profile[keys[0]])):
        max_v = 0
        max_k = None
        for k in keys:
            v = profile[k][i]
            if v > max_v:
                max_v = v
                max_k = k
        result.append(max_k)
    return ''.join(result)


# large_dataset = open('dataset/rosalind_gc.txt').read()
# large_dataset = fasta(large_dataset)
small_dataset="""
                    ATCCAGCT
                    GGGCAACT
                    ATGGATCT
                    AAGCAACC
                    TTGGAACT
                    ATGCCATT
                    ATGGCACT
                """
strings=""
sequences = []
with open('dataset/rosalind_cons.txt', 'r') as fin:
    sequence = ''
    for line in fin:
        if line.startswith('>'):
            sequences.append(sequence)
            sequence = ''
        else:
            sequence =sequence+ line
sequences.remove('')
for x in sequences:
    strings+=sequence

p = profile(small_dataset)
# c = consensus(p)

# print (c)
# for k in sorted(p):
#     print ("%s: %s" % (k, ' '.join(map(str, p[k]))))

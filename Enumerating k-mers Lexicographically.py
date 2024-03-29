def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    res.sort()
    return res

small_dataset = "T A G C\n2"
large_dataset = open('dataset/rosalind_lexf.txt').read()
bits = large_dataset.split()
alphabet = bits[:-1]
comb_len = int(bits[-1])
for p in alpha_combs(alphabet, comb_len):
    print (p)

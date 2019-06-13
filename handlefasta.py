#%%
import sys

#assign label into key and record base of label from fasta format
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

def gc_content(s):
	n = len(s)
	m = 0

	for c in s:
		if (c == 'G' or c == 'C' or c=='c' or c=='g'):
			m += 1

	return (100 * (float(m) / n))


large_dataset = open('Enterococcus_genome.fasta').read()

results = fasta(large_dataset)
results = dict([(k, gc_content(v)) for k, v in results.items()])

highest_k = None
highest_v = 0



for k, v in results.items():
	if v > highest_v:
		highest_k = k
		highest_v = v

print (results)
print (highest_k)
print (highest_v)

#%%

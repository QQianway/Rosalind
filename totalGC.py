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

def totalGC(s):
	totalLen=0
	totalGC=0
	for k ,v in s.items():
		totalLen+=len(v)
		for c in v:
			if (c == 'G' or c == 'C' or c=='c' or c=='g'):
				totalGC += 1
	return (100 * (float(totalGC) / totalLen))


large_dataset = open("D:/LAM/python/Enterococcus_genome.fasta").read()

results = fasta(large_dataset)

print('Total GC content is ', totalGC(results))

GCresults = dict([(k, gc_content(v)) for k, v in results.items()])
print (GCresults)
#%%

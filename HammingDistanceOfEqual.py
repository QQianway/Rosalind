import sys
def hammingDist(str1,str2):
	i=0
	count=0
	for x in str1:
		if (str1[i]!=str2[i]):
			count+=1
		i+=1;
	return count;

str1="GAGCCTACTAACGGGAT"
str2="CATCGTAATGACGGCCT" 
count=hammingDist(str1,str2)
print(count)
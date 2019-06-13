#Finding protein motif
import urllib.request
import os

# Parses FASTA-formatted data assuming a single line ID and a multi-line string
# Outputs a list - IDs are followed by their corresponding string
def parse_fasta(data):
    raw_datalist = data.splitlines()
    datalist = []
    for line in raw_datalist:
        if line.startswith(">"):
            datalist.append(line)
            datalist.append("")
        else:
            datalist[-1] += line
    return datalist

# Searches a single string for the glycmotif N{P}[ST]{P}
# Outputs a tuple: first value is True or False (presence), second value is positions of motif if true (otherwise blank list) 
def search_glycmotif(string):
    pos = []
    present = False
    for i in range(0, len(string)-3):
        if string[i] == "N" and string[i+1] != "P" and string[i+2] in ("S", "T") and string[i+3] != "P":
            pos.append(i+1)
            present = True
    return (present, pos)


with open('dataset/rosalind_mprt.txt') as file:
    idlist = file.read().splitlines()

alldata = []

for item in idlist:
    raw = urllib.request.urlopen("http://www.uniprot.org/uniprot/{}.fasta".format(item)).read()
    curr_entry = parse_fasta(raw.decode("utf-8"))
    for value in curr_entry:
        alldata.append(value)

for i in range(1, len(alldata), 2):
    search_result = search_glycmotif(alldata[i])
    if search_result[0]:
        print(idlist[int((i-1)/2)])
        for j in range(len(search_result[1])):
            if j < len(search_result[1]) - 1:
                print(search_result[1][j], end=" ")
            else:
                print(search_result[1][j])
# Open files
with open("rosalind_lcsm.txt", "r") as file:
    data = file.readlines()
result = open("lcsm.txt", "w")

# Main codes
seqs = {}
for i in data:
    if i[0] == ">":
        seqs[i[1::].strip()] = ""
    else:
        seqs[list(seqs.keys())[-1]] += i.strip()
n = len(min(list(seqs.values())))
for i in range(n, 0, -1):
    for seq in seqs.values():
        

# Close files
result.close()

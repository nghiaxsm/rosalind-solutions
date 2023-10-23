import time
start = time.time()
# Open files
with open("rosalind_lcsm.txt", "r") as file:
    data = file.readlines()
result = open("lcsm.txt", "w")

# Main codes
# Extract all given sequences
seqs = {}
for i in data:
    if i[0] == ">":
        seqs[i[1::].strip()] = ""
    else:
        seqs[list(seqs.keys())[-1]] += i.strip()
# Extract all sub sequences
min_seq = min(list(seqs.values()))
n = len(min_seq)
subseqs = []
for i in range(n,1,-1):
    for j in range(0,n-i+1):
        subseqs.append(min_seq[j:j+i])
# Fidn common substring
def common_sub(seqs, sub):
    return all(sub in seq for seq in seqs)
# Find longest common sub-sequence
def longest_common(seqs):
    
    
# Close files
result.close()

end = time.time()
print((end-start)*10**3, "ms")
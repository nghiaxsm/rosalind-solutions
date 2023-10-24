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
# Check if a sub sequence in all sequences
def sub_in_all(sub, seqs):
    return all(sub in seq for seq in seqs)
# Find longest common
l = 0
min_seq = min(list(seqs.values()))
r = len(min_seq)
motif = ""
while l < r:
    mid = (l + r) // 2
    print(l, mid, r)
    for i in range(0, len(min_seq) - mid + 1):
        subseq = min_seq[i:i+mid]
        if sub_in_all(subseq, seqs.values()) == True:
            print(len(subseq))
            l = mid
            motif = subseq
        else:
            r = mid
    print("222", l, mid, r)
print(motif)
print(len(motif))
result.write(motif)
# Close files
result.close()

end = time.time()
print((end-start)*10**3, "ms")
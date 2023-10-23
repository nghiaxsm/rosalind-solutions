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
# Extract all possible sub sequences
min_seq = min(list(seqs.values()))
n = len(min_seq)
sub_seqs = []
for i in range(n,1,-1):
    for j in range(0,n-i+1):
        sub_seqs.append(min_seq[j:i+j])
# Find longest common subsequences by binary search
l = 0
r = len(sub_seqs)
found = False
def sub_in_all(sub, seqs):
    for seq in seqs:
        if sub not in seq:
            return False
    return True

while found == False and l + 1 > mid :
    for seq in seqs:
        mid = (l + r) // 2
        if sub_in_all(sub_seqs[mid], seqs) == True:
            r = mid
        else:
            l = mid            
            
    
# Close files
result.close()

end = time.time()
print((end-start)*10**3, "ms")
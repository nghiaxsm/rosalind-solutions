# Open files
with open("rosalind_grph.txt", "r") as file:
    data = file.readlines()
result = open("graph.txt", "w")

# Main codes
seqs = {}
for i in data:
    if i[0] == ">":
        seqs[i[1::].strip()] = ""
    else:
        seqs[list(seqs.keys())[-1]] += i.strip()
def digr(node1, node2):
    s1 = node1[-3:]
    s2 = node2[:3]
    if s1 == s2:
        return True
    else:
        return False
for key1 in seqs.keys():
    for key2 in seqs.keys():
        if key1 != key2 and digr(seqs[key1],seqs[key2]):
            result.write(key1 + " " + key2 + "\n")        

# Close files
result.close()
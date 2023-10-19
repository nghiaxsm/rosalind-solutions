# Open files
with open("rosalind_gc.txt", "r") as file:
    data = file.readlines()
result = open("gc.txt", "w")

# Main codes
seqs = {}
for i in data:
    if i[0] == ">":
        seqs[i[1::].strip()] = ""
    else:
        seqs[list(seqs.keys())[-1]] += i.strip()
def gc_cont(seq):
    total = len
gc_content = []

print(seqs)
        

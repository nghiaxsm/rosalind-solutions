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
    total = len(seq)
    gc_count = 0
    for i in seq:
        if i in ["G", "C"]:
            gc_count += 1
    return gc_count / total * 100
max_seq = ''
max_gc = 0
for key, value in seqs.items():
    if gc_cont(value) > max_gc:
        max_seq = key
        max_gc = gc_cont(value)
result.write(max_seq + "\n" + str(round(max_gc, 6)))

# Close files
result.close()
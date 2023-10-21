# Open files
with open("rosalind_cons.txt", "r") as file:
    data = file.readlines()
result = open("cons.txt", "w")

# Main codes
## Import the sequences
seqs = {}
for i in data:
    if i[0] == ">":
        seqs[i[1::].strip()] = ""
    else:
        seqs[list(seqs.keys())[-1]] += i.strip()
## Create profile matrix
n = len(list(seqs.values())[0])
profile = {
    "A": [0] * n,
    "C": [0] * n,
    "G": [0] * n,
    "T": [0] * n,
}
for value in seqs.values():
    for i in range(len(value)):
        profile[value[i]][i] += 1
## Create consensus sequence
cons = ""
for i in range(n):
    max = 0
    cons_nu = "A"
    for nu in profile.keys():
        if profile[nu][i] > max:
            cons_nu = nu
            max = profile[nu][i]
    cons += cons_nu
result.write(cons)            

# Close files
result.close()

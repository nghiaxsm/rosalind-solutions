# Open files
with open("rosalind_rna.txt", "r") as file:
    data = file.readline().strip()
result = open("rna.txt", "w")

# Main codes
rna = ''
for nu in data:
    if nu == "T":
        rna += "U"
    else:
        rna += nu
result.write(rna)

# Close files
result.close()
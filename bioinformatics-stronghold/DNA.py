# Open files
with open("rosalind_dna.txt", "r") as file:
    data = file.readline()
result = open("dna.txt", "w")

# Main codes
nu = dict((k, 0) for k in ("A", "C", "G", "T"))
for i in data.strip():
    nu[i] += 1
for value in nu.values():
    result.write(str(value) + " ")    

# Close files
result.close()

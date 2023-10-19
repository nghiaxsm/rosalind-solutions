# Open files
with open("rosalind_revc.txt", "r") as file:
    data = file.readline().strip()
result = open("revc.txt", "w")

# Main codes
comp = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
}
revc = ""
for nu in data:
    revc = ''.join((comp[nu], revc))
result.write(revc)

# Close files
result.close()
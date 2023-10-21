# Open files
with open("rosalind_hamm.txt", "r") as file:
    data = file.readlines()
result = open("hamm.txt", "w")

# Main codes
s = data[0].strip()
t = data[1].strip()
n = len(s)
d = 0
for i in range(n):
    if s[i] != t[i]:
        d += 1
result.write(str(d))

# Close files
result.close()

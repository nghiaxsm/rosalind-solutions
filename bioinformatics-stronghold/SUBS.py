# Open files
with open("rosalind_subs.txt", "r") as file:
    data = file.readlines()
result = open("subs.txt", "w")

# Main codes
s = data[0].strip()
t = data[1].strip()
pos = []
for i in range(0, len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        pos.append(i+1)
result.write(" ".join(str(i) for i in pos))

# Close files
result.close()

# Open files
with open("rosalind_ini5.txt", "r") as file:
    data = file.readlines()
result = open("ini5.txt", "w")

# Main code
for i in range(len(data)):
    if i % 2 == 1:
        result.write(data[i])

# Close files
result.close()

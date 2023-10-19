# Open files
with open("rosalind_ini6.txt", "r") as file:
    data = file.readline()
result = open("ini6.txt", "w")

# Main code
words = data.split()
dict = {}
for word in words:
    if word in dict.keys():
        dict[word] += 1
    else:
        dict[word] = 1
for key, value in dict.items():
    s = key + " " + str(value) + "\n"
    result.write(s)

# Close files
result.close()
# Open files
with open("rosalind_ini3.txt", "r") as file:
    data = file.readlines()
result = open("ini3.txt", "w")

# Main codes
string = str(data[0])
numbers = [int(x) for x in data[1].split()]
a, b, c, d = numbers
s1 = string[a:b + 1]
s2 = string[c:d + 1]
s = s1 + " " + s2
result.write(s)

# Close files
result.close()

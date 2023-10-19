# Open files
with open("rosalind_ini2.txt", "r") as file:
    data = file.readline()
result = open("ini2.txt", "w")

# Main code
numbers = [int(x) for x in data.split()]
a = numbers[0]
b = numbers[1]
c = a*a + b*b
result.write(str(c))

# Close files
result.close()
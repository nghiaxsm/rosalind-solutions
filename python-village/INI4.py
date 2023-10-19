# Open files
with open("rosalind_ini4.txt", "r") as file:
    data = file.readline()
result = open("ini4.txt", "w")

# Main code
numbers = [int(x) for x in data.split()]
a = numbers[0]
b = numbers[1]
total = 0
for i in range(a, b+1):
    if i % 2 == 1:
        total = total + i
result.write(str(total))

# Close files
result.close()

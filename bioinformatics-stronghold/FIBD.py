# Open files
with open("rosalind_fibd.txt", "r") as file:
    data = file.readline().strip().split()
result = open("fibd.txt", "w")

# Main codes
n = int(data[0])
m = int(data[1])
fibd = [1] + [0]*(m-1)
for i in range(n-1):
    new_born = sum(fibd[1:])
    fibd[1:] = fibd[0:-1]
    fibd[0] = new_born
result.write(str(sum(fibd)))

# Close files
result.close()
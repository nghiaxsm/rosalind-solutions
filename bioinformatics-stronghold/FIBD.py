# Open files
with open("rosalind_fibd.txt", "r") as file:
    data = file.readline().strip().split()
result = open("fibd.txt", "w")

# Main codes
n = int(data[0])
m = int(data[1])
def fibd(n, m):
    print(n, m)
    if n == 1 or n == 2:
        return 1
    elif n < m:
        return fibd(n-1, m) + fibd(n-2, m)
    else:
        return fibd(n-1, m) + fibd(n-2,m) - fibd(n-m, m)
result.write(str(fibd(n, m)))

# Close files
result.close()
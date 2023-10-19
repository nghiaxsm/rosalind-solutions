# Open files
with open("rosalind_fib.txt", "r") as file:
    data = file.readline().strip().split()
result = open("fib.txt", "w")

# Main codes
n = int(data[0])
k = int(data[1])
def fib(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1, k) + k * fib(n - 2, k)
result.write(str(fib(n, k)))       
# Close files
result.close()
# Open files
with open("rosalind_iprb.txt", "r") as file:
    data = file.readline().strip()
result = open("iprb.txt", "w")

# Main codes
numbers = [int(i) for i in data.split()]
k, m, n = numbers
total = k + m + n
i = k*(k-1)+m*(m-1)*3/4+n*(n-1)*0+2*(k*m+m*n*1/2+n*k)
t = total*(total-1)
prob = i / t
result.write("{:.5f}".format(prob))

# Close files
result.close()
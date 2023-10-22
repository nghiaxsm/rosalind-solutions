# Open files
with open("rosalind_iev.txt", "r") as file:
    data = file.readline().split()
result = open("iev.txt", "w")

# Main codes
PROB = [1, 1, 1, 0.75, 0.50, 0]
dom_num = 0
for i in range(len(data)):
    dom_num += 2 * int(data[i].strip()) * PROB[i]
result.write(str(dom_num))
    
# Close files
result.close()

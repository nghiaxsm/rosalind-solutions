# Open files
with open("rosalind_prot.txt", "r") as file:
    data = file.readline().strip()
result = open("prot.txt", "w")

# Main codes
CODON = {
    "F":["UUU", "UUC"], "L":["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], "S":["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], "Y":["UAU", "UAC"], "Stop":["UAA", "UAG", "UGA"], "C":["UGU", "UGC"], "W":["UGG"],"P":["CCU", "CCC", "CCA", "CCG"], "H":["CAU", "CAC"], "Q":["CAA", "CAG"], "R":["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "I":["AUU", "AUC", "AUA"], "M":["AUG"], "T":["ACU", "ACC", "ACA", "ACG"], "N":["AAU", "AAC"], "K":["AAA", "AAG"], "V":["GUU", "GUC", "GUA", "GUG"], "A":["GCU", "GCC", "GCA", "GCG"], "D":["GAU", "GAC"], "E":["GAA", "GAG"], "G":["GGU", "GGC", "GGA", "GGG"]
}
aa_list = list(CODON.keys())
codon_list = list(CODON.values())
aa_seq = ""
for i in range(0,len(data), 3):
    aa = data[i:i+3]
    index = 0
    while aa not in codon_list[index]:
        index += 1
    if aa_list[index] == "Stop":
        break
    else:
        aa_seq += aa_list[index]
result.write(aa_seq)

# Close files
result.close()
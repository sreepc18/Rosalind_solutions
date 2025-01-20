f = open(r"C:\Users\pcsre\Downloads\rosalind_dna(5).txt", "r")
a=0
t=0
g=0
c=0
for file in f:
    a = file.count("A")
    t= file.count("T")
    g= file.count("G")
    c= file.count("C")

print(f"{a} {c} {g} {t}")



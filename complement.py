
f= open(r"C:\Users\pcsre\Downloads\rosalind_revc(2).txt","r")
for c in f:
    c = c.strip()  # Remove trailing newline or spaces
    print(len(c))  # Print original sequence length
    print(c)  # Print original sequence

    # Reverse the sequence
    s = c[::-1]
    print(s)  # Print reversed sequence
    # Get the reverse complement
    s1 = ""

    for k in s:
        if k=="A":
            s1+="T"
        elif k=="T":
            s1+="A"
        elif k=="G":
            s1+="C"
        elif k=="C":
            s1+="G"
        

print(s1)
print(len(s1))
f.close()



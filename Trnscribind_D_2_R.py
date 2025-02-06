f=open(r"C:\Users\pcsre\Downloads\rosalind_rna(1).txt","r")#opening file in reading mode

dna=f.readline()
ans=""#make an empty string for adding nucleotides

for k in dna:
    if k=="T" :
        ans+="U"
    else:
        ans+=k

print(ans)
f.close()
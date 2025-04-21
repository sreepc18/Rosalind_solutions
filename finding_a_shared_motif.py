"""A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k
(k≤100

) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
Sample Dataset

>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output

AC"""
from Bio import SeqIO

sequences = []                             
handle = open(r"C:\Users\pcsre\Downloads\rosalind_lcsm(3).txt", "r")     
for record in SeqIO.parse(handle, 'fasta'):
    sequence = []                          
    seq = ''                               
    for nt in record.seq:                  
        seq += nt                          
    sequences.append(seq)                  
handle.close() 

srt_seq = sorted(sequences, key=len)     
short_seq = srt_seq[0]                   
comp_seq = srt_seq[1:]                   
motif = ''                               
for i in range(len(short_seq)):          
    for j in range(i, len(short_seq)):   
        m = short_seq[i:j + 1]           
        found = False                    
        for sequ in comp_seq:            
            if m in sequ:                
                found = True             
            else:                        
                found = False            
                break                    
        if found and len(m) > len(motif):
            motif = m                    
print(motif)  

print(len(motif))    




my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT" 

exon1 = my_dna[0:62] 
intron = my_dna[62:90].lower()
exon2 = my_dna[90:10000] 

print(exon1 + intron + exon2)

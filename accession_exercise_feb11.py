import re 

dna = open("dna.txt").read().rstrip("\n") 
print(str(len(dna))) 
everything = [0] 

#Positions for AbcI 
for match in re.finditer(r"A[ATGC]TAAT",dna): 
	everything.append(match.start() + 3) 

#Positions for AbcII
for match in re.finditer(r"GC[AG][AT]TG",dna): 
	everything.append(match.start() + 4) 

#Final position 
everything.append(len(dna)) 
sorted_cuts = sorted(everything) 
print(sorted_cuts) 

for i in range(1,len(sorted_cuts)): 
	big_cut = sorted_cuts[i] 
	small_cut = sorted_cuts[i-1] 
	fragment_size = big_cut - small_cut
	print("one fragment size is " + str(fragment_size))

file = open("input.txt") 

output = open("trimmed.txt", "w") 
for dna in file:
	character_position = len(dna) 
	trimmed_dna = dna[14:character_position] 
	output.write(trimmed_dna) 

print("length of sequence: " + str(len(trimmed_dna)))


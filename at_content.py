my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" 

length = len(my_dna) 
a_count = my_dna.count('A') 
t_count = my_dna.count('T') 

at_calc = (a_count + t_count)/length

print a_count
print t_count
print length
print at_calc

print("AT content is " + str(at_calc))


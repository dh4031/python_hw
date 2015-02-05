from __future__ import division
import string

def get_at_content(dna):
#used replace string to remove N and n from the dna string
	true_dna = dna.replace('n''N','');
#use the new variable that contains the true count of just ATCG
	length = len(true_dna)
	a_count = true_dna.upper().count('A')
	t_count = true_dna.upper().count('T')
	at_content = (a_count + t_count) / length
	return at_content

my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCATGCAACTGTAGC"))
print(get_at_content("aactgtagctagctagcagcgta"))
print(get_at_content("TTCGNNN"))
print(get_at_content("ttcgnnn"))


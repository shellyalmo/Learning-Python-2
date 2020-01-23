"""In this project I'm using files methods to do DNA analysis for a crime investigation.
The program's parts are:
1) Given a file, read in the DNA for each suspect and save it as a string.
2) Take a DNA string and split it into a list of codons.
3) Iterate through a suspect’s codon list to see how many of their codons match the sample codons.
4) Pick the right suspect to continue the investigation on. """

# One small DNA sample was successfully retrieved from the computer’s keyboard. The program will match these codons to the suspects’ DNA samples.
sample = ['GTA','GGG','CAC']

# A method that will read a suspect’s DNA sample.
# It will take in a file, read it, add the file’s contents to an empty string, and return the updated string.
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file,'r') as f:
    for line in f:
      dna_data += line
  return dna_data

# A method that will take a string, create a list of codons from that string, and return the list. 
# This will make the DNA analysis much easier later.
def dna_codons(dna):
  codons = []
  for i in range(0,len(dna),3):
    #check if the iterator, when incremented by 3, exceeds the length of dna.
    if (i+3) < len(dna):
      codons.append(dna[i:i+3])
  return codons

# A method that will iterate through both the sample and a suspect’s DNA. 
# The method counts the number of times a codon in the sample matches a codon in the suspect’s DNA.
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

# A method that uses the other methods to determine who the criminal is.
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "Number of matches found: {}. The investigation should continue.".format(num_matches)
  else:
    print "Number of matches found: {}. The suspect can go free.".format(num_matches)
    
    
is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')
# The correct answer is suspect 2 with 6 matching codons.
  
  
      
    
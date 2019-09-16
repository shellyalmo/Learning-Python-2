"""This program is a Pig Latin translator. Any word you type in will be converted to the Pig Latin equivalent."""

#This variable contains the addition to the word
pyg = 'ay'

#This variable contains the input word from the user
original = raw_input('Enter a word:')

#converting the input word to lower case
word = original.lower()

#making sure the input contains only characters
if len(original) > 0 and original.isalpha():
  print word
else:
  print 'empty'
  
#This variable contains the first letter of the word
first = word[0]

#This variable is concatenating the word, it's first letter and the suffix 'ay'
new_word = word + first + pyg

#This variable contains the word after the concatenation, and without the first letter.
new_word = new_word[1:len(new_word)]

print new_word

"""This program is demonstrating the usage of nested loops and inner and outer lists. In this program, the function gets a list that contains inner lists and loops through all of them to create a new list."""

#The outer list that contains two inner lists.
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

#This function loops through the outer list and then through each inner list, and appends the numbers in a new list.
def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
     results.append(number)
    
  return results
    
print flatten(n)

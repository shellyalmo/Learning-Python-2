"""This program is calculating how much you’re paying for all of the items on your grocery list"""

#The inventory information
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
#The prices information
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

#This function gets the grocery list and calculates the total cost, in addition to updating the stock info
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total
 
#Testing the function 
grocery_list = ["apple","pear","banana","orange","orange","banana"]
print compute_bill(grocery_list)
print stock

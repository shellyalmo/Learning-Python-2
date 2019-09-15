"""This program is calculating the total cost of a trip, including hotel, rental car, plane ticket and extra expenses."""

#This function calculates the hotel cost by number of nights.
def hotel_cost(nights):
  return 140*nights

#This function calculates the cost of the plane ticket, depending on the destination.
def plane_ride_cost(city):
  if city=="Charlotte":
    return 183
  elif city=="Tampa":
    return 220
  elif city=="Pittsburgh":
    return 222
  elif city=="Los Angeles":
    return 475

#This function calculates the cost of renting a car, by the number of days.  
def rental_car_cost(days):
    cost = 40*days
    if days>=7:
      cost-=50
    elif days>=3:
      cost-=20
    return cost
      
# This function calculates the total cost of the trip, including all the expenses.    
def trip_cost(city,days,spending_money):
  return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city) + spending_money
  
#testing each function in the case of a trip to Los Angeles for 5 days and spending extra 600$.
print hotel_cost(5-1)
print plane_ride_cost("Los Angeles")
print rental_car_cost(5)
print trip_cost("Los Angeles",5,600)

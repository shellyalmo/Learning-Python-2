"""This program is helping teachers to create a gradebook for the students in class."""

#Each student's info is stored in a dictionary.
#Each dictionary contains lists of info.
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

#This is the list of students in the class.
students = [alice,lloyd,tyler]

#This function takes a list of numbers and returns the average.
def average(numbers):
  total = sum(numbers)
  total = float(total)
  result = total/len(numbers)
  return result

#This function takes a student dictionary as input and returns the weighted average.
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  #The weight is: Homework is 10%, quizzes are 30% and tests are 60%.
  return 0.1*homework + 0.3*quizzes + 0.6*tests

#This function takes a number score as input and returns a string with the letter grade that that student should receive.
def get_letter_grade(score):
  if score>=90:
    return "A"
  elif score>=80 and score<=89:
    return "B"
  elif score>=70 and score<=79:
    return "C"
  elif score>=60 and score<=69:
    return "D"
  else:
    return "F"

#This function gets the average for each student and then calculates the average of those averages.
def get_class_average(class_list):
  results =[]
  for student in class_list:
    result = get_average(student)
    #Appending that value to the results list using .append
    results.append(result)
  return average(results)

#Testing the functions.
print get_letter_grade(get_average(tyler))
print get_class_average(students)
#Testing - calculating the letter grade for the class’s average
print get_letter_grade(get_class_average(students))   

# For Loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)

# AVERAGE HEIGHT EXERCISE
# Write a program that calculates the average student height from a List of heights without using sum() or len()
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#print(student_heights)

# solution  using sum () and len()
# number_students = len(student_heights)
# sum_height = sum(student_heights)
# avg_height = round(sum_height/number_students)
# print(avg_height

# Replicate how the sum() works
total_height = 0
for height in student_heights:
  total_height += height

#Replicate how len() works
num_students = 0
for student in student_heights:
  num_students += 1

average_height = round(total_height / num_students)
print(average_height)
# FOR LOOPS
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)

# AVERAGE HEIGHT EXERCISE
# Write a program that calculates the average student height from a List of heights without using sum() or len()
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#print(student_heights)

# solution  using sum () and len()
# number_students = len(student_heights)
# sum_height = sum(student_heights)
# avg_height = round(sum_height/number_students)
# print(avg_height

# Replicate how the sum() works
# total_height = 0
# for height in student_heights:
#   total_height += height

# Replicate how len() works
# num_students = 0
# for student in student_heights:
#   num_students += 1

# average_height = round(total_height / num_students)
# print(average_height)



# HIGH SCORE EXERCISE
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Don't use the max() or min ()
# print(max(student_scores))
# print(min(student_scores))

# Replicate how max works ()
#Initialize the max value to the first element.
# max_score = student_scores[0]
# Iterate through the list, and if we find a larger value than the current max, we assign that value to max
# for score in student_scores:
#   if score > max_score:
#     max_score = score
# print(f"The highest score in the class is: {max_score}")

# another solution
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")
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
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

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
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
# print(f"The highest score in the class is: {highest_score}")



# FOR LOOPS AND THE RANGE() FUNCTION
# total = 0
# for number in range(1, 101):
#   total += number
# print(total)



# ADDING EVENS EXERCISE
#Write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100. i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# sum_even = 0
# for number in range(2,101,2):
#   sum_even += number
# print(sum_even)


# FIZZBUZZ EXERCISE ** TOP INTERVIEW QUESTION
# for number in range(1,101):
#   if number % 3 == 0 and number % 5 == 0:
#     number = "FizzBuzz"
#     print(str(number))
#   elif number % 3 == 0:
#     number = "Fizz"
#     print(str(number))
#   elif number % 5 == 0:
#     number = "Buzz"
#     print(str(number))
#   else:
#     print(str(number))

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
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

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
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
# print(f"The highest score in the class is: {highest_score}")



# FOR LOOPS AND THE RANGE() FUNCTION
# total = 0
# for number in range(1, 101):
#   total += number
# print(total)



# ADDING EVENS EXERCISE
#Write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100. i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# sum_even = 0
# for number in range(2,101,2):
#   sum_even += number
# print(sum_even)


# FIZZBUZZ EXERCISE ** TOP INTERVIEW QUESTION
# for number in range(1,101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)



# EASY LEVEL - PW GENERATOR
#store empty pw string
password = ""

# loop through all of the characters, generate a range based on user input
for char in range(1, nr_letters + 1):
  #generate random letter for each position
  random_char = random.choice(letters)
  # add random character to pw
  password += random_char

for char in range(1, nr_symbols + 1):
  random_sym = random.choice(symbols)
  password += random_sym

for char in range(1, nr_numbers + 1):
  random_num = random.choice(numbers)
  password += random_num

print(f"Here is your new password: {password}")
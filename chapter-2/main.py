# Rosendo Lugo Jr.
# Chapter 2 Programming
# Personal Grade Calculator

# This program calculates the final grade in percentage
# using 4 assignments and 2 test.

# Assign how much an assignment is worth.
assignment_worth = .45

# Assign how much a test is worth.
test_worth = .55

# Get the assignment scores from the user.
assignment1 = int(input('Enter assignment 1 grade (0-100): '))
assignment2 = int(input('Enter assignment 2 grade (0-100): '))
assignment3 = int(input('Enter assignment 3 grade (0-100): '))
assignment4 = int(input('Enter assignment 4 grade (0-100): '))

# Combine all the assignments into one equation.
total_assignments = ((assignment1 + assignment2 + assignment3 + assignment4)/4)

# Calculate the assignments worth.
total_assignments_worth = total_assignments * assignment_worth

# Get the test scores from the user.
test1 = int(input('Enter test 1 grade (0-100): '))
test2 = int(input('Enter test 2 grade (0-100): '))

# Combine all the tests into one equation.
total_tests = ((test1 + test2)/2)

# Calculate the assignments worth.
total_tests_worth = total_tests * test_worth

# Calculate the final grade by adding the
# total_assignments and total_tests
final_grade = (total_assignments_worth + total_tests_worth)/100

# Display the final grade in percentage.
print(f'Final grade: {final_grade:.2f}')



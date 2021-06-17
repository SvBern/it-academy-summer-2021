# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  2 to 5, print Not Weird
# If  is even and in the inclusive range of  6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

n = int(input('Enter a number between 1 and 100 inclusive\n'))
if 1 <= n <= 100:
    if n % 2 == 1:
        print('Weird')
    else:
        if 2 <= n <= 5 or n > 20:
            print('Not weird')
        elif 6 <= n <= 20:
            print('Weird2')
else:
    print('Bad n')

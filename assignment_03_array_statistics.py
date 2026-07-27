# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def calculate_sum(numbers):
    total = 0
    for value in numbers:
        total = total + value
    return total



def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average


def calculate_maximum(numbers):
    maximum = numbers[0]
    for value in numbers:
        if value > maximum:
            maximum = value
    return maximum

def calculate_minimum(numbers):
    minimum = numbers[0]
    for value in numbers:
        if value < minimum:
            minimum = value
    return minimum


n = int(input("How many numbers? "))
if n <= 0:
    print("Error: Please enter a positive integer.")
    exit()

numbers = []
for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

total_sum = calculate_sum(numbers)
average = calculate_average(numbers)
maximum = calculate_maximum(numbers)
minimum = calculate_minimum(numbers)

print("Results:")
print(f"Sum:  {total_sum}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
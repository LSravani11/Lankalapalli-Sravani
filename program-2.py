#enter a number
a = int(input("input a = "))

# Start with 1 (first odd number)
number = 1

# Creating an empty list to store the numbers
result = []

# Generate 'a' odd numbers
for i in range(a):
    result.append(str(number))  # Add current number to the list (as a string)
    number += 2  # Go to next odd number

# Print output in required format
print("output :", ", ".join(result))

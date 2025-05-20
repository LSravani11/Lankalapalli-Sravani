# for input
a = int(input("input a = "))

# If 'a' is even, reduce it by 1
if a % 2 == 0:
    a -= 1

# Start with the first odd number
number = 1
result = []

# Generate 'a' odd numbers (only for odd a)
for i in range(a):
    result.append(str(number))
    number += 2  

# Print the result i
print("output :", ", ".join(result))

# Input list 
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

#dictionary to store results
result = {}

# Loop t each from 1 to 9
for i in range(1, 10):
    count = 0  # to count how many numbers are divisible by i
    for num in numbers:
        if num % i == 0:
            count += 1
    result[i] = count  

# Print the result
print(result)

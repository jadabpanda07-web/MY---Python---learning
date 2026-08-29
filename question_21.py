numbers = [12, 4, 56, 7, -3, 45, 0]

# Start with the first element
smallest = numbers[0]
largest = numbers[0]

# Loop through the list
for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)

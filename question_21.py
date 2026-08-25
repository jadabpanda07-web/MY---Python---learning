# Find the largest and smallest element in a list without using max() and min()
numbers = []

n = int(input('Enter the number of elements: '))

for i in range(n):
    element = float(input('Enter an element: '))
    numbers.append(element)

if not numbers:
    print('The list is empty.')
else:
    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    print('Smallest element:', smallest)
    print('Largest element:', largest)
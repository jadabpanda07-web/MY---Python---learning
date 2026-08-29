n = int(input('Enter a number:'))

list = []

for i in range(n):
    element = input('Enter a element in list: ')
    list.append(element)

even_numbers = []
odd_numbers = []
for num in list:
    if int(num) % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
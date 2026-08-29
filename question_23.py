# find the second largest number in a list

n = int(input('Enter a number:'))

list = []

for i in range(n):
    element = int(input('Enter a element in list: '))
    list.append(element)

list = sorted(list)
print("Second largest number:", list[-2])


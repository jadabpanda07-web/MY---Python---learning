# Rotate a list by k position

n = int(input("Enter a number: "))

# Create a list using loop
list = []

for i in range(n):
    element = input('Enter a element in list: ')
    list.append(element)



k = int(input("Enter a position: "))

for i in range(k):
    last = list.pop()
    list.insert(0,last)

print(list)
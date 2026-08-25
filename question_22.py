# remove duplicate element from a list

n = int(input('Enter a number:'))

list = []

for i in range(n):
    element = input('Enter a element in list: ')
    list.append(element)

# remove duplicates
list = (set(list))
print("List after removing duplicates:", list)
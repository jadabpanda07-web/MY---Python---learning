# Reverse a list without using the reverse() or slicing method

#create an user input list
n = int(input('Enter a number:'))   

list = []

for i in range(n):
    element = input('Enter a element in list: ')
    list.append(element)

# reverse a list
reversed_list = []

for i in range(len(list)-1,-1,-1):
    reversed_list.append(list[i])

print('reversed list is ',reversed_list)    

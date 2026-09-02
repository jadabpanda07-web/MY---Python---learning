# Find the frequency of every element in list

n = int(input("Enter a number: "))

list = []
for i in range(n):
    value = int(input("Enter element: "))
    list.append(value)

for i in list:
    print(f"Frequency of {i} element ", list.count(i))
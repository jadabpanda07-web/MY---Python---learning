# merge two lists and remove duplicates

l1 = [1,2,3,4,5]
l2 = [4,5,8,9,10]

list = []
for i in l1:
    if i not in list:
        list.append(i)
for i in l2:
    if i not in list:
        list.append(i)

print(list)



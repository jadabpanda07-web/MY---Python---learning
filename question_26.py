# Find common elements b/w two list

l1 = [1,2,3,4,5]
l2 = [4,5,8,9,7]

common = []

for i in l1:
    if i in l2:
        common.append(i)

print(common)
    
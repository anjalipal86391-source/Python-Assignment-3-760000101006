list1 = [10, 20, 30]

# Using copy()
list2 = list1.copy()

# Using direct assignment
list3 = list1

list1.append(40)

print("Original list =", list1)
print("Copied list =", list2)
print("Assigned list =", list3)
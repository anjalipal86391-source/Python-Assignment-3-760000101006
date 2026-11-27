numbers = [10, 20, 30, 40, 50]

element = int(input("Enter element: "))
position = int(input("Enter position: "))

numbers.insert(position, element)

print("Updated list =", numbers)
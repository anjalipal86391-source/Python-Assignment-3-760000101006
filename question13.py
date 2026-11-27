text = input("Enter a string: ")
ch = input("Enter a character: ")

if text.startswith(ch) and text.endswith(ch):
    print("String starts and ends with", ch)
else:
    print("String does not start and end with", ch)
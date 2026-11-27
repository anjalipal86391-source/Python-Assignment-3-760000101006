text = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0

for ch in text:
    if ch.isdigit():
        digits = digits + 1
    elif ch.isalpha():
        alphabets = alphabets + 1
    else:
        special = special + 1

print("Digits =", digits)
print("Alphabets =", alphabets)
print("Special Characters =", special)
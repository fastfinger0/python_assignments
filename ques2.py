var = input("Enter a string: ")

alphabets = 0
numbers = 0

for char in var:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        numbers += 1

print(f"Alphabets: {alphabets} & Number: {numbers}")
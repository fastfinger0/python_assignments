start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

sum = 0
for num in range(start, stop + 1):
    if num % 2 != 0:
        sum += num

print(f"Sum of odd numbers: {sum}") #
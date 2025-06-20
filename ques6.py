number = int(input("Enter a number: "))
sum_of_divisors = 0

if number <= 0:
    print("No")
else:
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number:
        print("Yes, it is a perfect number.")
    else:
        print("No") #
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result_lcm = lcm(number1, number2)
print(f"LCM of {number1} and {number2} are: {result_lcm}") 
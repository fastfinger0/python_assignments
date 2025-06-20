def sum_digits(num):
    current_sum = num
    while current_sum >= 10:
        sum_of_digits = 0
        for digit in str(current_sum):
            sum_of_digits += int(digit)
        current_sum = sum_of_digits
    return current_sum

num = int(input("Enter a number: "))
first_sum = sum(int(digit) for digit in str(num))
print(f"Sample Input: num = {num}") # 
print(f"Sample Output: Sum_of_digits = {first_sum},") # 

final_output = sum_digits(num)
print(f"Final Output: {final_output}") #
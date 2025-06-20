phy = float(input("Enter marks for Physics: "))
chem = float(input("Enter marks for Chemistry: "))
bio = float(input("Enter marks for Biology: "))
math = float(input("Enter marks for Mathematics: "))
computer = float(input("Enter marks for Computer: "))

total_marks = phy + chem + bio + math + computer
percentage = (total_marks / 500) * 100

print(f"Total Percentage: {percentage:.2f}%")

if percentage >= 90:
    grade = 'A' 
elif percentage >= 80:
    grade = 'B' 
elif percentage >= 70:
    grade = 'C' 
elif percentage >= 60:
    grade = 'D' 
elif percentage >= 40:
    grade = 'E' 
else:
    grade = 'F'  

print(f"Grade: {grade}")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

sorted_string1 = sorted(string1.lower())
sorted_string2 = sorted(string2.lower())

if sorted_string1 == sorted_string2:
    print(True) 
else:
    print(False)
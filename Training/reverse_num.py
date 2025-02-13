# using slicer by taking the number as a string input

# number = input("Enter a number")
# print(number[::-1])

#2nd method -->

value=0
number = int(input("Enter a number"))
while number >1:
    unit = number%10
    number = number//10
    value = unit+value*10
print(value)
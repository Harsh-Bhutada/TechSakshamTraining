number = int(input("Enter a number"))
if (number%5==0) and (number%2==0):
    print("Number is divisible by 5 and is an even number")
else:
    if (number%5==0):
        print("Number is divisible by 5 but not an even number")
    else:
        print("Number is not divisble by 5")
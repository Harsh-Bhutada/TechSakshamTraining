number = int(input("Enter a number"))
i=2
counter=0
while i <= number:
    if number%i==0:
        counter+=1
    i+=1
if counter == 1:
    print(number, " is a prime number")
else:
    print(number," is not a prime number")
number = int(input("Enter a number"))
i=1
factor = []
while i <= number:
    if number%i==0:
        factor.append(i)
    i+=1
print(factor)
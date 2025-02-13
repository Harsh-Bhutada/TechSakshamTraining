bill = int(input("Enter the bill amount"))
tip = int(input("Enter the tip percentage"))
no_of_people = int(input("Enter the number of people"))
# Calculating the total amount to be paid by each person
pay_per_person = (bill/no_of_people)*(100+tip)/100
print("Each person has to pay ", pay_per_person)
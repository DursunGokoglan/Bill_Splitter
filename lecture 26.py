print("Welcome to the bill splitter!")

currency = input("What is the currency?\n")
bill = float(input("What is the total bill?\n"))
tip_percentage = float(input("What percentage tip would you like to give?\n"))
number_of_people = int(input("How many people to split the bill?\n"))

total = bill + (bill*tip_percentage/100)

each_pays = total / number_of_people
rounded_each_pays = round(each_pays, 2)

print(f"Each person should pay {currency} {rounded_each_pays}.")
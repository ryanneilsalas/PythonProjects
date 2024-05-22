print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
number_people = input("How many people to split the bills? ")
real_tip = float(tip) / 100
result_tip = float(total) * (1 + real_tip)
result = "{:.2f}".format(result_tip / int(number_people))
print(f"Each person should pay: ${result}")

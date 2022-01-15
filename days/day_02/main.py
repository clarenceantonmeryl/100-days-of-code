

print("Welcome to the tip calculator.")
'''
total_cost_before_tip = float(input("What was the total bill? $"))
number_of_people = float(input("How many people to split the bill? "))
percentage_tip = float(input("What percentage tip would you like to give? "))

total_cost = total_cost_before_tip * (1 + (percentage_tip / 100))

result = round(total_cost / number_of_people,2)

result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")

'''
a = int("5") / int(2.7)

print(a)

print(6 + 4 / 2 - 2)

"""


print(123_456_789_101_123 + 123_456)

num = input("Type a two digit number: ")

if isinstance(num, str) and len(num) == 2:

    str(num)

    num_digit_1 = int(num[0])

    num_digit_2 = int(num[1])

    result = num_digit_1 + num_digit_2

    print(result)
else:
    print("Write a two digit number")



bmi = float(input("Enter your bmi: "))
height = float(input("Enter your height in m: "))

weight = bmi * (height ** 2)

print(weight)



weight = float(input("Enter your weight: "))
height = float(input("Enter your height in m: "))

bmi = round(weight / (height ** 2),2)

print(bmi)


age = int(input("What is your age? "))

years_left = 90 - age

months_left = years_left * 12

weeks_left = years_left * 52

days_left = years_left * 365

print(f"You have {days_left} days left. You have {weeks_left} weeks left. You have {months_left} months left.")

"""
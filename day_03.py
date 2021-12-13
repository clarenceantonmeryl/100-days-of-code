
"""

print("Welcome to treasure island\nYour mission is to find the treasure.")
cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.").lower()

if cross_road == "right":
    print("You die")
elif cross_road == "left":
    lake = input("You come to a lake. Do you swim or wait for a boat? Type 'wait' or 'swim'").lower()

    if lake == "wait":
        door = input("You arrive to the island and find 3 houses with 3 coloured doors (red, blue, yellow). What house do you pick. Type 'red', 'blue' or 'yellow'").lower()

        if door == "red":
            print("You found the treasure.")

        elif door == "blue":
            print("You die.")

        elif door == "yellow":
            print("You die.")
        else:
            print("Wrong answer. You die anyway.")

    elif lake == "swim":
        print("You die")

    else:
        print("Wrong answer. You die anyway.")

else:
    print("Wrong answer. You die anyway.")


price = 0

size = input("What size pizza do you want? S, M or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

if size == "s":
    price = 15
elif size == "m":
    price = 20
elif size == "l":
    price = 25
else:
    print("Size does not exist")

if add_pepperoni == "y":
    if size == "s":
        price += 2
    else:
        price += 3

if extra_cheese == "y":
    price += 1

print(f"Price: ${price}.")


"""

first_name = input("Enter the first name: ").lower()
second_name = input("Enter the second name: ").lower()

combined_name = first_name + second_name

t = int(combined_name.count("t"))
r = int(combined_name.count("r"))
u = int(combined_name.count("u"))
e = int(combined_name.count("e"))

first_number = int((t + r + u + e) * 10)


l = int(combined_name.count("l"))
o = int(combined_name.count("o"))
v = int(combined_name.count("v"))
e = int(combined_name.count("e"))

second_digit = int(l + o + v + e)

result = first_number + second_digit

print(f"Score: {result}")

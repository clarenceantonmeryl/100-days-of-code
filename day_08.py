import math

def paint_calculator(height, width, coverage):
    cans = math.ceil((height * width) / coverage)
    print(f"You'll need {cans} cans")


height = int(input("What is the height of the wall: "))
width = int(input("What is the width of the wall: "))
coverage = 5

paint_calculator(height=height, width=width, coverage=coverage)
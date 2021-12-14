def add(num1, num2):
    result = num1 + num2
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result


def multiply(num1, num2):
    result = num1 * num2
    return result


def divide(num1, num2):
    if num2 == 0:
        print("cannot divide by 0")
    else:
        result = num1 / num2
        return result


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    calculating = True

    num1_input = float(input("What is your first number? "))

    while calculating:

        for symbol in operations:
            print(symbol)

        operator_input = input("What operation do you want to perform? ")
        num2_input = float(input("What is your second number? "))

        output = 0

        output = operations[operator_input](num1=num1_input, num2=num2_input)

        print(f"{num1_input} {operator_input} {num2_input} = {output}")

        next_step = input("Press 'c' continue, 's' to start fresh, 'x' to exit: ").lower()

        if next_step == "x":
            calculating = False
            return
        elif next_step == "s":
            calculating = False
            calculator()
        else:
            num1_input = output


calculator()
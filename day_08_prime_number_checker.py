def prime_number_checker(number):

    divisible_count = 0

    if number == 0 or number == 1:
        print("It's not a prime number")

    else:
        is_prime = True
        for index in range(2, number):
            if number % index == 0:
                print("It's not a prime number")
                is_prime = False
                break

        if is_prime:
            print("It's a prime number.")


while True:
    number = int(input("Enter number: "))

    prime_number_checker(number=number)

    if number == 0:
        break

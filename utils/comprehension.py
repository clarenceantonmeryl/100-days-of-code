#  new_list = [new_item for item in existing_list if condition]

#  new_list = [new_item for (key, value) in existing_dictionary.items() if condition]


fruits_dict = {
    'key_0': "Apple",
    'key_1': "Orange",
    'key_2': "Apricot",
    'key_3': "Mango",
}

list_from_dict = [value for (key, value) in fruits_dict.items() if key != 'key_1']

print(list_from_dict)


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytrippler = myfunc(3)

print(mydoubler(11))
print(mytrippler(11))


def display_grade(grade: str) -> int:
    match grade:
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3
        case _:
            return 0


display_grade("F")


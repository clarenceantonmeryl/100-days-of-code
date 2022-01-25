'''
# LIST COMPREHENSION

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

# LAMBDA FUNCTION

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytrippler = myfunc(3)

print(mydoubler(11))
print(mytrippler(11))

# SWITCH CASE

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


# INT DIVISION

result = 13 // 4
print(result)
# 3

# FLOOR DIVISION

result = 15.0 // 2.2
print(result)
# 6.0

# ESCAPING

x = "He said \"You are amazing\" yesterday."




# DYNAMIC STRING FORMATTING

name = "Tomas"
age = 13

string_format_1 = f"Hello {name}, you are {age} years old"
string_format_2 = "Hello {}, you are {} years old"
string_format_3 = "Hello {name}, you are {age} years old"

print("\nFirst print set:")
print(string_format_1)
print(string_format_2.format(name, age))
print(string_format_3.format(name=name, age=age))

name = "Moses"
age = 10

print("\nSecond print set:")
print(string_format_1)
print(string_format_2.format(name, age))
print(string_format_3.format(name=name, age=age))

a = f"""hello {name}
how are you doing?"""

print(a)



# BOOLEAN
# and :
# first true and second true => second
# first false and second true => first
# or  :
# first true and second true => first
# first false and second true => second

print(bool(0))                                      # False
print(bool(3))                                      # True
print(bool(-3))                                     # True
print(bool(""))                                     # False
print(bool("A"))                                    # True

print(35 and 40)                                    # 40
print(35 and True)                                  # True
print(35 and False)                                 # False
print(0 and 40)                                     # 0
print(0 and False)                                  # 0
print(0 and True)                                   # 0
print(True and False)                               # False
print(False and True)                               # False
print(True and 40)                                  # 40
print(False and 40)                                 # False

print(35 or 40)                                     # 35
print(0 or 40)                                      # 40

print(0 or "")                                      # ""
print("" or 0)                                      # 0

print(35 or "")                                     # 35
print("" or 40)                                     # 40


cmp = 15 > 20 or 17 < 20
print(cmp)                                          # True

age = 16
side_job = True
print(age > 18 and age or side_job)                 # True


# TUPPLE

friends = ("Tomas", "Moses", "Josh")
friends = friends + ("Jaden", )

print(friends)

# SETS - No duplicate allowed and no order is guaranteed

art_class = {"Lavanth", "Dhruv"}
art_class.add("Movid")

print(art_class)                                    # {'Dhruv', 'Movid', 'Lavanth'}

science_class = {"Clarence", "Dhruv", "Charlie"}

print(art_class.difference(science_class))          # 'art not scienc' {'Lavanth', 'Movid'}

print(art_class.symmetric_difference(science_class)) # 'art not in both'

print(art_class.intersection(science_class))        # intersection of set

print(art_class.union(science_class))               # union of set



def var_scope():
    a = int(input("Enter a val: "))
    if a > 5:
        b = "greater than 5"
    print(b)


var_scope()

'''




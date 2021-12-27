import random

# # numbers = [1, 2, 3, 20, 50, 40 , 1820, 20, 591, 6902, 2394928]
# # new_list = [n**15 for n in numbers]
# # print(new_list)
# # #
# # # name = "Human"
# # # new_list = [letter for letter in name]
# # # print(new_list)
# #
# # numbers = [number * 2 for number in range(1, 5) if number % 2 == 0]
# # print(numbers)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if "z" not in name or "x" not in name]
# print(long_names)
#
# with open(file="file_1.txt", mode="r") as file_1:
#     file_1_numbers = file_1.readlines()
#
# with open(file="file_2.txt", mode="r") as file_2:
#     file_2_numbers = file_2.readlines()
#
# # stripped_list_1 = [int(number.strip()) for number in file_1_numbers]
# # stripped_list_2 = [int(number.strip()) for number in file_2_numbers]
#
# final_list = [int(number.strip()) for number in file_1_numbers if number in file_2_numbers]
# print(final_list)

# names = ["Alex", "Jonte", "Micheal", "Dave", "Eleanor", "Freddie"]
#
# student_scores = {name: random.randint(0, 50) for name in names}
# print(student_scores)
#
# scores_above_75 = {key: value * 2 for (key, value) in student_scores.items() if value > 25}
# print(scores_above_75)

# sentence = "What,is,the,Airspeed,velocity,of,an,Unladen,Swallow?"
#
# words = sentence.split(",")
# words = [word.replace("?", "") for word in words]
#
# result = {word: len(word) for word in words}
#
# print(result)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: round(weather * 1.8 + 32, 1) for (day, weather) in weather_c.items()}
# print(weather_f)

import pandas

student_dict = {
    "student": ["Thomas", "Moses", "Almond"],
    "score": [396, 689, 129]
}
student_data_frame = pandas.DataFrame(student_dict)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(f"{row.student}, {row.score}")

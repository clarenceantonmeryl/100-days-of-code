import csv
# with open(file="weather_data.csv", mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# print(data.temp.mean())
#
# print(data.day.min())
#
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp * 1.8 + 32)

data = pandas.read_csv("Squirrel_Data.csv")
grey_amount = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_amount = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_amount = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Amount": [grey_amount, cinnamon_amount, black_amount]
}

data_frame = pandas.DataFrame(data_dict)

data_frame.to_csv("squirrel.colors.csv")
# with open("weather_data.csv") as weather_file:
#     weather_data = weather_file.readlines()
#     print(weather_data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# # print(data_dict)
# # print(data["temp"])
# data_temp = data["temp"].to_list()
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
print((monday_temp * 9/5) + 32)

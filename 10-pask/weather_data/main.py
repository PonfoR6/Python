import csv
import pandas
from pprint import pprint

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()

temp_list = data["temp"].to_list()

average_temp = data["temp"].mean()
max_temp = data["temp"].max()
min_temp = data["temp"].min()

monday = data[data.day == "Monday"]

day_max_temp = data[data.temp == data.temp.max()]

monday_temp = int(monday.temp)
monday_condition = str(monday.condition)

data_to_csv = {
    "students": ["Q1", "Q2", "Q3"],
    "grades": [2, 2, 2]
}

data_frame = pandas.DataFrame(data_to_csv)
data_frame.to_csv("students.csv")
# print(monday_temp)
# print(monday_condition)
# print(day_max_temp)
# print(monday)
# print(average_temp)
# print(min_temp)
# print(max_temp)
# print(temp_list)
# pprint(data_dict)
# print(type(data))
# print(data)

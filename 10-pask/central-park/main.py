import pandas

data = pandas.read_csv("central_park_squirrels.csv")
# grey_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
# cin_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_sq_count = len(data[data["Primary Fur Color"] == "Black"])
#
# adult_sq = len(data[data["Age"] == "Adult"])
# juvenile_sq = len(data[data["Age"] == "Juvenile"])
# unkwn_sq = len(data[data["Age"] == "?"])

# hghlght_black_sq = len(data[data["Highlight Fur Color"] == "Black"])
# hghlght_cin_sq = len(data[data["Highlight Fur Color"] == "Cinnamon"])
# hghlght_gray_sq = len(data[data["Highlight Fur Color"] == "Gray"])
# hghlght_white_sq = len(data[data["Highlight Fur Color"] == "White"])
# hghlght_unkwn_sq = len(data) - (hghlght_white_sq + hghlght_gray_sq + hghlght_cin_sq + hghlght_black_sq)

running_true_sq = len(data[data["Running"] == True])
running_false_sq = len(data[data["Running"] == False])
chasing_true_sq = len(data[data["Chasing"] == True])
chasing_false_sq = len(data[data["Chasing"] == False])
climbing_true_sq = len(data[data["Climbing"] == True])
climbing_false_sq = len(data[data["Climbing"] == False])
eating_true_sq = len(data[data["Eating"] == True])
eating_false_sq = len(data[data["Eating"] == False])
foraging_true_sq = len(data[data["Foraging"] == True])
foraging_false_sq = len(data[data["Foraging"] == False])

#
# print(grey_sq_count)
# print(cin_sq_count)
# print(black_sq_count)

# print(adult_sq)
# print(juvenile_sq)
# print(unkwn_sq)

# print(hghlght_black_sq)
# print(hghlght_cin_sq)
# print(hghlght_gray_sq)
# print(hghlght_white_sq)
# print(hghlght_unkwn_sq)

print(running_true_sq)
print(running_false_sq)
print(chasing_true_sq)
print(chasing_false_sq)
print(climbing_true_sq)
print(climbing_false_sq)
print(eating_true_sq)
print(eating_false_sq)
print(foraging_true_sq)
print(foraging_false_sq)

# data_dict = {
#     "Fur Color": ["Grey", "Cinnamon", "Black"],
#     "Count": [grey_sq_count, cin_sq_count, black_sq_count]
#
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("sq_count.csv")

# 1
# f = open("uzduotis1.txt", "r")
# print(f.read())
# f.close()

# 2
# f = open("uzduotis2.txt", "a")
# f.write('heyo')
# f.close()

# 3
# f = open("uzduotis1.txt", "r")
# print(f.readlines())

# 4
# with open("uzduotis4.txt") as file:
#     data = file.read().replace('\n', '')

# 11
# with open("copy.txt") as file1:
#     with open("paste.txt", "w") as file:
#         for line in file1:
#             file.write(line)

# 6
# def longest_word(filename):
#     with open(filename, "r") as infile:
#         word = infile.read().split()
#         max_len = len(max(word, key=len, ))
#         return [word for word in word if len(word) == max_len]
#
#
# print(longest_word('uzduotis4.txt'))

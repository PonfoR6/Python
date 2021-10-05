import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

vardas = input("Irasykite varda: ")
list_of_letters = list(vardas)

# print(list_of_letters)
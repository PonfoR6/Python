import os

PLACEHOLDER = "[name]"


def check_if_names_exist():
    if os.path.exists("./names") and os.path.exists("names/names.txt"):
        return True
    else:
        print("names not found")
        return False


def check_if_letter_exists():
    if os.path.exists("letter") and os.path.exists("./letters/letter.txt"):
        return True
    else:
        print("letters not found")
        return False


if not check_if_names_exist() and not check_if_letter_exists():
    exit()

with open("./names/names.txt") as name_file:
    names = name_file.readlines()
    print(names)

with open('./letter/letter.txt') as letter_file:
    letter_content = letter_file.read()

    if os.path.exists("output"):
        print("Folder not found, creating new one.")
        os.mkdir("output")

    print("letters are generating")

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

    with open(f"./output/b-day-wish-{stripped_name.lower()}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)

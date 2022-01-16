def addition():
    print("Addition")
    n = float(input("Enter the number: "))
    ans = 0
    while n != 0:
        ans = ans + n
        n = float(input("Enter another number (0 to calculate): "))
    return [ans]


def subtraction():
    print("Subtraction")
    x = float(input("Enter the number: "))
    y = float(input("Enter another number"))
    ans = x - y
    return [ans]


def multiplication():
    print("Multiplication")
    n = float(input("Enter the number: "))
    ans = 1
    while n != 0:
        ans = ans * n
        n = float(input("Enter another number (0 to calculate): "))
    return [ans]


def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans]


while True:
    list = []
    print("python calculator")
    print(" Enter 'a' for addition")
    print(" Enter 's' for subtraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0])
        else:
            print("Sorry, invalid character")
    else:
        break

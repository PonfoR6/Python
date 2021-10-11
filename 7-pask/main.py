import random

livesRemaining = 5


def main():
    global livesRemaining


difficulty = input(f"Welcome! Choose the difficulty level: easy, medium, hard, impossible ")

if difficulty == "easy":
    n = random.randint(1, 10)
    guess = int(input(f"Input a number between 1-10: "))
    while n != guess:
        if guess > n:
            print(f"🠗")
            guess = int(input(f"Input a number between 1-10: "))
            livesRemaining -= 1
            print(f"You have {livesRemaining} lives remaining")
        elif guess < n:
            print(f"🠕")
            guess = int(input(f"Input a number between 1-10: "))
            livesRemaining -= 1
            print(f"You have {livesRemaining} lives remaining")
        elif guess == n:
            print(f"✓")
            break
        if livesRemaining == 0:
            print(f"Out of lives. The Number was {n}")
            break

if difficulty == "medium":
    n = random.randint(1, 50)
    guess = int(input(f"Input a number between 1-50: "))
    while n != guess:
        if guess > n:
            print(f"🠗")
            livesRemaining -= 1
            print(f"You have {livesRemaining} lives remaining")
        elif guess < n:
            print(f"🠕")
            guess = int(input(f"Input a number between 1-50" ))
            livesRemaining -= 1
            print(f"You have {livesRemaining} lives remaining" )
        elif guess == n:
            print("✓")
            break
        if livesRemaining == 0:
            print(f"Out of lives. The Number was {n}")
            break

if difficulty == "hard":
    n = random.randint(1, 100)
    guess = int(input(f"Input a number between 1-100: "))
    while n != guess:
        if guess > n:
            print(f"🠗")
            guess = int(input(f"Input a number between 1-100 "))
            livesRemaining -= 1
            print(f"You have {livesRemaining} lives remaining")
        elif guess < n:
            print(f"🠕")
            guess = int(input(f"Input a number between 1-100 "))
            livesRemaining -= 1
            print(f"You have {livesRemaining} lives remaining")
        elif guess == n:
            print("✓")
            break
        if livesRemaining == 0:
            print(f"Out of lives. The Number was {n}")
            break

if difficulty == "impossible":
    n = random.randint(1, 1000)
    guess = int(input(f"Input a number between 1-1000: "))
    if n != guess:
        print(f"Out of lives. The Number was {n}")


import random

num = random.randint(1,10)
UserInput = int(input("Enter a number between 1 to 10: "))
Guess_Count = 0
while num != UserInput:
    UserInput = int(input("Enter a number between 1 to 10: "))
    Guess_Count += 1

print(f"Congratulation you have guessed the number in {Guess_Count} times")
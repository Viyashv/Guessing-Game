import random
print("Rules of the game:")
print("1. The game will randomly Generate a number between 1 and 20.")
print("2. The user has to guess the number.")
print("3. Every guess will increase the guess count by 1.")
print("4. The game will end when the user guesses the number correctly")
print("Game Start...")
num = random.randint(1,20)
print(num)
Guess_Count = 0
UserInput = int(input("Start Enter a number between 1 to 20: "))
Guess_Count += 1
while True:
    try:
        if UserInput < num:
            print(f"Guess a litte high than {UserInput}")
            UserInput = int(input("High Enter a number between 1 to 20: "))
            Guess_Count += 1
        elif UserInput > num:
            print(f"Guess a little low than {UserInput}")
            UserInput = int(input("Low Enter a number between 1 to 20: "))
            Guess_Count += 1
        else:
            break
    except ValueError as e:
        print("Invalid input. Please enter a number between 1 to 20")
    

print(f"Congratulation you have guessed the number in {Guess_Count} times")
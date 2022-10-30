import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input('Type Rock/Paper/Scissor or Q to quite: ').lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Compter picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("The user win")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("The user win")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("The user win")
        user_wins += 1

    elif user_input =="rock" and computer_pick == "rock":
        print("Tie")

    elif user_input == "paper" and computer_pick == "paper":
        print("Tie")

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Tie")

    else:
        print("The Computer win")
        computer_wins += 1

print("users wins = " , user_wins)
print("computer wins" , computer_wins)
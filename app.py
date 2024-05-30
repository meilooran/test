import random

user_wins = 0
computer_wins = 0

options = ["камень", "бумага", "ножницы"]

while True:
    user_input = input("Выбери Камень/Бумага/Ножницы или В для выхода: ").lower()
    if user_input == "d":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Компьютер выбрал", computer_pick + ".")

    if user_input == "камень" and computer_pick == "ножницы":
        print("You won!")
        user_wins += 1

    elif user_input == "ножницы" and computer_pick == "камень":
        print("You lost!")
        computer_wins += 1

    elif user_input == "бумага" and computer_pick == "камень":
        print("You won!")
        user_wins += 1

    elif user_input == "камень" and computer_pick == "бумага":
        print("You lost!")
        computer_wins += 1

    elif user_input == "ножницы" and computer_pick == "бумага":
        print("You won!")
        user_wins += 1

    elif user_input == "бумага" and computer_pick == "ножницы":
        print("You lost!")
        computer_wins += 1

    else:
        print("Ничья")


print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
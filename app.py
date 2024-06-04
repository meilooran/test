import random

user_wins = 0
computer_wins = 0

options = ["камень", "бумага", "ножницы"]

while True:
    user_input = input("Выбери Кам./Бум./Нож. или 0 для выхода: ").lower()
    if user_input == "0":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Компьютер выбрал", computer_pick + ".")

    if user_input == "камень" and computer_pick == "ножницы":
        print("Ты выиграл!")
        user_wins += 1

    elif user_input == "ножницы" and computer_pick == "камень":
        print("Ты проиграл!")
        computer_wins += 1

    elif user_input == "бумага" and computer_pick == "камень":
        print("Ты выиграл!")
        user_wins += 1

    elif user_input == "камень" and computer_pick == "бумага":
        print("Ты проиграл!")
        computer_wins += 1

    elif user_input == "ножницы" and computer_pick == "бумага":
        print("Ты выиграл!")
        user_wins += 1

    elif user_input == "бумага" and computer_pick == "ножницы":
        print("Ты проиграл!")
        computer_wins += 1

    else:
        print("Ничья")

print("Ты выиграл", user_wins, "раз.")
print("Компьютер выиграл", computer_wins, "раз.")

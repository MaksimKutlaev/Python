def choose_game():
    print(f"Выберите игру \nXO - 1\ncandies - 2")
    return int(input(f"Введите 1 или 2: "))

# def choose_game():
#     print(f"Выберите игру \nXO - 1\ncandies - 2")
# valid = False
# while not valid:
#     player_answer = input(f"Введите 1 или 2: ")
#     try:
#         player_answer = int(player_answer)
#         if player_answer >= 1 and player_answer <= 2:
#             valid = True
#         else:
#             print("Такой игры нет.\nНекорректный ввод. Введите 1 или 2")
#     except:
#         print("Некорректный ввод. Введите число")
#         continue
# choose_game()
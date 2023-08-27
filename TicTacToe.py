# Инациализация игрового поля (доски)
board = list(range(1, 10))
# Инациализация победных комбинаций
win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


# Выводим на экран игровое поле
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


# Перечислим условия для соблюдения правильности ходов
def take_input(step):
    while True:
        # Вводим только числа!
        answer = input("Куда поставить " + step + "? ")
        try:
            answer = int(answer)
        except ValueError:
            print("Вы ввели не число!")
            continue
        # Вводим числа только в свободные ячейки от 1 до 9!
        if 1 <= answer <= 9:
            if str(board[answer - 1]) not in "XO":
                board[answer - 1] = step
                break
            else:
                print("Эта клетка уже занята!")
        else:
            print("Выберите незанятую позицию от 1 до 9!")


# Проверка выигрышных комбинаций на поле
def check_win(board):
    for each in win_comb:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


# Главная функция, рисующая ходы и проверяющая выигрышные комбинации
# Определяет победителя и выводит сообщение и поле
def main(board):
    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0:  # Первым ходит - Х!
            take_input("X")
        else:
            take_input("O")
        counter += 1

        temp = check_win(board)
        if temp:
            print(temp, "выиграл!")
            break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)

input("Нажмите Enter для выхода!")
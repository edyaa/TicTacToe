from random import choice


class TicTacToe:
    def __init__(self):
        self.flag = False

        self.board_size = int(input('\nВведите размер сетки: '))
        while self.board_size <= 2:
            self.board_size = int(input('Неверное значение! Введите число >= 3: '))

        self.user_sign = input('Введите X или O (1 / 2): ')
        while self.user_sign not in list('12'):
            self.user_sign = input('Неверное значение! Введите 1 или 2: ')
        self.user_sign = 'X' if self.user_sign == '1' else 'O'
        self.computer_sign = 'X' if self.user_sign == 'O' else 'O'
        self.size_list = list(range(1, self.board_size**2 + 1))
        print('\n')

    def computer_move(self):
        free_cell = [x for x in self.size_list if x not in list('XO')]
        move = choice(free_cell)
        self.size_list[move - 1] = self.computer_sign
        self.flag = False

    def user_move(self):
        move = int(input('Выберите клетку: '))
        if move <= 0 or move > board_size**2:
            move = int(input('Введите число, не выходящее за пределы!: '))
        while self.size_list[move - 1] in list('XO'):
            move = int(input('Клетка занята! Введите свободную клетку: '))
        self.size_list[move - 1] = self.user_sign
        self.flag = True

    def print_board(self):
        for i in range(len(self.size_list)):
            print("| {:>2} ".format(str(self.size_list[i])), end='')
            if (i + 1) % self.board_size == 0:
                print('|')
                print('\n')

    def check_win(self):
        win_combinations = []
        i = 1
        j = 1
        size = self.board_size
        for _ in range(size):
            gorizontal = [i + x for x in range(size)]
            vertical = [j + x for x in range(0, size ** 2, size)]
            i += size
            j += 1
            win_combinations.append(gorizontal)
            win_combinations.append(vertical)

        first_diagonal = [1 + (size + 1) * x for x in range(size)]
        second_diagonal = [size + (size - 1) * x for x in range(size)]
        win_combinations.append(first_diagonal)
        win_combinations.append(second_diagonal)

        for i in range(2 + 2 * size):
            check = [self.size_list[x - 1] for x in win_combinations[i]]
            if len(set(check)) == 1:
                return True
        return False

    def win(self, check, count):

        winner = 'Пользователь' if check == True else 'Компьютер'
        print('-' * 30)
        print(f"\nПобедил: {winner} за {count} хода(-ов)")


    def game(self):
        i = 0
        while True:
            print('-' * 30 + '\n')
            self.print_board()

            self.user_move()
            print('\n')
            i += 1
            if i == self.board_size**2:
                print('-' * 30)
                print('\nНичья')
                break

            if self.check_win() == True:
                self.win(self.flag, i)
                break

            self.computer_move()
            i += 1
            if i == self.board_size**2:
                print('-' * 30)
                print('\nНичья')
                break

            if self.check_win() == True:
                self.win(self.flag, i)
                break


test = TicTacToe()
test.game()


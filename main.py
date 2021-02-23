from queue import Queue


class CMove:
    def __init__(self):
        self.__line_played = 0
        self.__column_played = 0
        self.__active_player = 1

    def set_Move(self, player, line, column):
        self.__active_player = player
        self.__line_played = line
        self.__column_played = column

    def get_player(self):
        return self.__active_player

    def get_column(self):
        return self.__column_played

    def get_line(self):
        return self.__line_played


class TicTacToe:
    def __init__(self):
        self.__grid = [['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']]
        self.__player = 1
        self.__turn = 0
        self.__history = Queue(9)

    def get_player(self):
        return self.__player
    
    def get_turn(self):
        return self.__turn

    def get_box(self, line, column):
        return self.__grid[line][column]

    def reset_grid(self):
        self.__grid = [['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']]

    def reset_player(self):
        self.__player = 1

    def change_player(self):
        if self.__player == 1:
            self.__player = 2
        else:
            self.__player = 1

    def play(self, line, column):
        """verifies if the player's line and column can be placed in the grid"""
        if line > 3 or line < 1 or column > 3 or column < 1:
            return False
        if self.__grid[line - 1][column - 1] != '-':
            return False
        if self.__player == 1:
            self.__grid[line - 1][column - 1] = 'X'
        else:
            self.__grid[line - 1][column - 1] = 'O'
        self.__turn += 1
        Move = CMove()
        Move.set_Move(self.__player, line, column)
        self.__history.queue(Move)
        return True

    def end_condition(self):
        """win conditions"""
        for i in range(3):
            if self.__grid[i][0] == self.__grid[i][1] == self.__grid[i][2] != '-':
                return True
        for i in range(3):
            if self.__grid[0][i] == self.__grid[1][i] == self.__grid[2][i] != '-':
                return True
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] != '-':
            return True
        if self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] != '-':
            return True
        return False

    def replay(self):
        """replay the game"""
        actual_move = self.__history.dequeue()
        self.play(actual_move.get_line(), actual_move.get_column())


def show_grid():
    for i in range(3):
        for j in range(3):
            print(TicTacToe.get_box(i, j), ' ', end='')
        print('')


TicTacToe = TicTacToe()

while TicTacToe.get_turn() != 9 and not TicTacToe.end_condition():
    while not TicTacToe.play(int(input("line? ")), int(input("column? "))):
        print("Error, replay.")
    show_grid()
    TicTacToe.change_player()
if not TicTacToe.end_condition():
    print("Draw!")
else:
    print("Player " + str(TicTacToe.get_player()) + " won!")
shistory = str(input("Do you want to look at the history? (yes or no) "))
total_moves = TicTacToe.get_turn()
while shistory == "yes":
    TicTacToe.reset_grid()
    TicTacToe.reset_player()
    actual_move = 0
    show_next_move = "yes"
    while actual_move < total_moves and show_next_move == "yes":
        TicTacToe.replay()
        TicTacToe.change_player()
        show_grid()
        actual_move += 1
        if actual_move < total_moves:
            show_next_move = str(input("Do you want to see the next move? (yes or no) "))
    if show_next_move == "yes":
        shistory = str(input("Do you want to rewatch the history? (yes or no) "))
    else:
        shistory = "no"

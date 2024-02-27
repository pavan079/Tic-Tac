import random

class TicTacToe:
    def __init__(self):
        # Define the initial board with empty spaces
        self.board = {1: ' ', 2: ' ', 3: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}

        # Set the player and computer markers
        self.player = 'O'
        self.computer = 'X'

    def print_board(self):
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-+-+-")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-+-+-")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("\n")

    def space_is_free(self, position):
        return self.board[position] == ' '

    def insert_letter(self, letter, position):
        if self.space_is_free(position):
            self.board[position] = letter
            self.print_board()

            if self.check_draw():
                print("Draw!")
                exit()

            if self.check_win():
                if letter == 'X':
                    print("Computer Bot wins!")
                else:
                    print("You Win! Congratulations!")
                exit()
        else:
            print("Invalid position or position already filled")
            position = int(input("Please re-enter a new position from 1-9: "))
            self.insert_letter(letter, position)

    def check_win(self):
        if (self.board[1] == self.board[2] == self.board[3] != ' ') or \
           (self.board[4] == self.board[5] == self.board[6] != ' ') or \
           (self.board[7] == self.board[8] == self.board[9] != ' ') or \
           (self.board[1] == self.board[4] == self.board[7] != ' ') or \
           (self.board[2] == self.board[5] == self.board[8] != ' ') or \
           (self.board[3] == self.board[6] == self.board[9] != ' ') or \
           (self.board[1] == self.board[5] == self.board[9] != ' ') or \
           (self.board[7] == self.board[5] == self.board[3] != ' '):
            return True
        return False

    def check_which_mark_won(self, mark):
        if (self.board[1] == self.board[2] == self.board[3] == mark) or \
           (self.board[4] == self.board[5] == self.board[6] == mark) or \
           (self.board[7] == self.board[8] == self.board[9] == mark) or \
           (self.board[1] == self.board[4] == self.board[7] == mark) or \
           (self.board[2] == self.board[5] == self.board[8] == mark) or \
           (self.board[3] == self.board[6] == self.board[9] == mark) or \
           (self.board[1] == self.board[5] == self.board[9] == mark) or \
           (self.board[7] == self.board[5] == self.board[3] == mark):
            return True
        return False

    def check_draw(self):
        for key in self.board.keys():
            if self.board[key] == ' ':
                return False
        return True

    def player_move(self):
        position = int(input("Enter a position for 'O' from 1-9: "))
        self.insert_letter(self.player, position)

    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def minimax(self, board, depth, is_maximizing):
        if self.check_which_mark_won(self.computer):
            return 1
        elif self.check_which_mark_won(self.player):
            return -1
        elif self.check_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = self.computer
                    score = self.minimax(board, depth + 1, False)
                    board[key] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = self.player
                    score = self.minimax(board, depth + 1, True)
                    board[key] = ' '
                    best_score = min(score, best_score)
            return best_score

    def comp_move_easy(self):
        available_moves = [key for key, value in self.board.items() if value == ' ']
        move = random.choice(available_moves)
        self.insert_letter(self.computer, move)

    def comp_move_hard(self):
        best_score = -float('inf')
        best_move = None
        for key in self.board.keys():
            if self.board[key] == ' ':
                self.board[key] = self.computer
                score = self.minimax(self.board, 0, False)
                self.board[key] = ' '
                if score > best_score:
                    best_score = score
                    best_move = key
        self.insert_letter(self.computer, best_move)

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        level = int(input("Choose a level:\n1. Easy\n2. Hard\nEnter your choice: "))
        if level != 1 and level != 2:
            print("Invalid choice. Setting level to easy.")
            level = 1

        while True:
            self.player_move()

            if level == 1:
                self.comp_move_easy()
            else:
                self.comp_move_hard()

            self.print_board()


game = TicTacToe()
game.play()

from tkinter import *
from tkinter import messagebox
import random
import copy

class XOGameAI:
    def __init__(self):
        self.board = [[" " for _ in range(4)] for _ in range(4)]

    def is_win(self, symbol):
        # Check rows and columns
        for i in range(4):
            if all(self.board[i][j] == symbol for j in range(4)) or \
               all(self.board[j][i] == symbol for j in range(4)):
                return True
        # Check diagonals
        if all(self.board[i][i] == symbol for i in range(4)) or \
           all(self.board[i][3 - i] == symbol for i in range(4)):
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def minimax(self, is_max):
        if self.is_win("O"):
            return 1
        elif self.is_win("X"):
            return -1
        elif self.is_draw():
            return 0

        scores = []
        for r in range(4):
            for c in range(4):
                if self.board[r][c] == " ":
                    self.board[r][c] = "O" if is_max else "X"
                    score = self.minimax(not is_max)
                    scores.append(score)
                    self.board[r][c] = " "

        return max(scores) if is_max else min(scores)

    def best_move(self):
        best_score = -float('inf')
        move = None
        for r in range(4):
            for c in range(4):
                if self.board[r][c] == " ":
                    self.board[r][c] = "O"
                    score = self.minimax(False)
                    self.board[r][c] = " "
                    if score > best_score:
                        best_score = score
                        move = (r, c)
        return move

class XOGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("XO 4x4 - Player vs AI")
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        self.game = XOGameAI()
        self.turn = "X"
        self.create_board()

    def create_board(self):
        for r in range(4):
            for c in range(4):
                btn = Button(self.root, text=" ", font=("Arial", 20), width=6, height=3,
                             command=lambda r=r, c=c: self.play(r, c))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

    def play(self, r, c):
        if self.buttons[r][c]["text"] == " " and self.turn == "X":
            self.buttons[r][c]["text"] = "X"
            self.game.board[r][c] = "X"
            if self.check_end("X"):
                return
            self.turn = "O"
            self.root.after(300, self.ai_turn)

    def ai_turn(self):
        move = self.game.best_move()
        if move:
            r, c = move
            self.buttons[r][c]["text"] = "O"
            self.game.board[r][c] = "O"
            if self.check_end("O"):
                return
        self.turn = "X"

    def check_end(self, symbol):
        if self.game.is_win(symbol):
            messagebox.showinfo("Game Over", f"{'You' if symbol == 'X' else 'AI'} wins!")
            self.disable_all()
            return True
        elif self.game.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_all()
            return True
        return False

    def disable_all(self):
        for r in range(4):
            for c in range(4):
                self.buttons[r][c]["state"] = DISABLED

if __name__ == "__main__":
    root = Tk()
    game = XOGameGUI(root)
    root.mainloop()
# So sánh 2 cách viết Minimax cho XO 4x4
# Tiêu chí	Cách viết của bạn (ban đầu)	Cách viết mới (lớp + AI riêng)
# Cấu trúc	Đơn giản, logic gắn trực tiếp với GUI	Rõ ràng, chia tách lớp xử lý và giao diện
# Dễ mở rộng	Khó mở rộng sang nhiều chế độ khác	Dễ mở rộng thêm Player vs Player, độ khó
# Hiệu năng	Tương đương	Tương đương
# Minimax	Đặt ngay trong GUI	Đặt trong class riêng (XOGameAI)
# Độ phức tạp code	Thấp hơn	Cao hơn một chút do tách class
# Giao diện	OK	Giao diện y như cũ
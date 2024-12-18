import tkinter as tk
from tkinter import messagebox

class tictactoe:
    def __init__(self):
        self.current_player="x"
        self.board=[["" for _ in range(3)]for _ in range(3)]

    def switch(self):
        self.current_player="o" if self.current_player=="x" else "x"

    def winner(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]!="":
                return True
            if self.board[0][i]==self.board[1][i]==self.board[2][i]!="":
                return True
        if self.board[0][0]==self.board[1][1]==self.board[2][2]!="":
            return True
        if self.board[0][2]==self.board[1][1]==self.board[2][0]!="":
            return True
        return False

    def draw(self):
        for row in self.board:
            if "" in row:
                return False
            return True

    def make_move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.current_player
            if self.winner():
                return f"Player {self.current_player} wins!"
            elif self.draw():
                return "It's a draw!"
            self.switch()
        return None

def click(row,col):
    result=game.make_move(row,col)
    buttons[row][col].config(text=game.board[row][col])
    if result:
        messagebox.showinfo("Game Over",result)

if __name__=="__main__":
    game = tictactoe()
    root=tk.Tk()
    root.title("Tic Tac Toe")
    buttons=[[None for _ in range(3)]for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]=tk.Button(root,text="",font=('normal',20),width=5,height=2,
                                        command=lambda r=row, c=col: click(r,c))
            buttons[row][col].grid(row=row,column=col)
    root.mainloop()

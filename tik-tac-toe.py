import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.current_player = "X"
        self.board = [""] * 9 
        
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", width=10, height=3, font=("Arial", 24),
            command=lambda i=i: self.tombol_klik(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        
        self.reset_button = tk.Button(root, text="Reset", width=20, height=2, font=("Arial", 16), command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=3)
        
        self.dev_label = tk.Label(root, text="Dev by: alyvers", font=("Arial", 12))
        self.dev_label.grid(row=4, column=0, columnspan=3)

    def tombol_klik(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.cek_menang():
                messagebox.showinfo("Tic Tac Toe", f"Pemain {self.current_player} menang!")
                self.reset()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "Seri! Tidak ada pemenang.")
                self.reset()
            else:
                self.switch_player()
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def cek_menang(self):
        menang_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        
        for combo in menang_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False
    
    def reset(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

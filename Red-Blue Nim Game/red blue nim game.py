import customtkinter as ctk
from tkinter import messagebox


class RedBlueNimGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Red-Blue Nim Game")
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self.root, text="Red-Blue Nim Game", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, columnspan=4, pady=10)

        self.red_label = ctk.CTkLabel(self.root, text="Red Marbles: ", font=("Arial", 14))
        self.red_label.grid(row=1, column=0, pady=5, sticky='e')
        self.red_count = ctk.CTkLabel(self.root, text="0", font=("Arial", 14))
        self.red_count.grid(row=1, column=1, pady=5, sticky='w')

        self.blue_label = ctk.CTkLabel(self.root, text="Blue Marbles: ", font=("Arial", 14))
        self.blue_label.grid(row=2, column=0, pady=5, sticky='e')
        self.blue_count = ctk.CTkLabel(self.root, text="0", font=("Arial", 14))
        self.blue_count.grid(row=2, column=1, pady=5, sticky='w')

        self.score_label = ctk.CTkLabel(self.root, text="Scores: ", font=("Arial", 14))
        self.score_label.grid(row=3, column=0, pady=5, sticky='e')
        self.score_value = ctk.CTkLabel(self.root, text="Human: 0, Computer: 0", font=("Arial", 14))
        self.score_value.grid(row=3, column=1, pady=5, sticky='w')

        self.message_label = ctk.CTkLabel(self.root, text="", font=("Arial", 14), wraplength=300)
        self.message_label.grid(row=4, column=0, columnspan=4, pady=10)

        self.red_move_label = ctk.CTkLabel(self.root, text="Red Marbles to remove: ", font=("Arial", 14))
        self.red_move_label.grid(row=5, column=0, pady=5, sticky='e')
        self.red_move = ctk.CTkEntry(self.root, width=50)
        self.red_move.grid(row=5, column=1, pady=5, sticky='w')

        self.blue_move_label = ctk.CTkLabel(self.root, text="Blue Marbles to remove: ", font=("Arial", 14))
        self.blue_move_label.grid(row=6, column=0, pady=5, sticky='e')
        self.blue_move = ctk.CTkEntry(self.root, width=50)
        self.blue_move.grid(row=6, column=1, pady=5, sticky='w')

        self.submit_move_button = ctk.CTkButton(self.root, text="Submit Move", command=self.human_move)
        self.submit_move_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.version_label = ctk.CTkLabel(self.root, text="Game Version: ", font=("Arial", 14))
        self.version_label.grid(row=1, column=2, pady=5, sticky='e')
        self.version_var = ctk.StringVar(value="standard")
        self.version_menu = ctk.CTkOptionMenu(self.root, values=["standard", "misere"], variable=self.version_var)
        self.version_menu.grid(row=1, column=3, pady=5, sticky='w')

        self.first_player_label = ctk.CTkLabel(self.root, text="First Player: ", font=("Arial", 14))
        self.first_player_label.grid(row=2, column=2, pady=5, sticky='e')
        self.first_player_var = ctk.StringVar(value="computer")
        self.first_player_menu = ctk.CTkOptionMenu(self.root, values=["computer", "human"],
                                                   variable=self.first_player_var)
        self.first_player_menu.grid(row=2, column=3, pady=5, sticky='w')

        self.start_button = ctk.CTkButton(self.root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=3, column=2, columnspan=2, pady=10)

    def reset_game(self):
        self.red_marbles = 10
        self.blue_marbles = 10
        self.human_score = 0
        self.computer_score = 0
        self.turn = None
        self.update_display()

    def start_game(self):
        self.reset_game()
        self.turn = self.first_player_var.get()
        self.message_label.configure(text=f"{self.turn.capitalize()} starts!")
        if self.turn == 'computer':
            self.computer_move()

    def update_display(self):
        self.red_count.configure(text=str(self.red_marbles))
        self.blue_count.configure(text=str(self.blue_marbles))
        self.score_value.configure(text=f"Human: {self.human_score}, Computer: {self.computer_score}")

    def human_move(self):
        try:
            red_move = int(self.red_move.get())
            blue_move = int(self.blue_move.get())
            if red_move < 0 or blue_move < 0 or red_move + blue_move == 0 or red_move + blue_move > 2:
                raise ValueError
            if red_move > self.red_marbles or blue_move > self.blue_marbles:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Move", "Invalid move. Please enter valid numbers of marbles to remove.")
            return
        self.red_marbles -= red_move
        self.blue_marbles -= blue_move
        self.check_game_over()
        self.turn = 'computer'
        self.update_display()
        self.computer_move()

    def computer_move(self):
        # Implement MinMax with Alpha Beta Pruning here
        pass

    def check_game_over(self):
        if self.red_marbles == 0 or self.blue_marbles == 0:
            if self.version_var.get() == "standard":
                winner = "Computer" if self.turn == "computer" else "Human"
            else:
                winner = "Human" if self.turn == "computer" else "Computer"
            self.calculate_score()
            messagebox.showinfo("Game Over",
                                f"Game Over! {winner} wins!\nFinal Score:\nHuman: {self.human_score}, Computer: {self.computer_score}")
            self.reset_game()

    def calculate_score(self):
        self.human_score = self.red_marbles * 2 + self.blue_marbles * 3
        self.computer_score = (10 - self.red_marbles) * 2 + (10 - self.blue_marbles) * 3


if __name__ == "__main__":
    root = ctk.CTk()
    game = RedBlueNimGame(root)
    root.mainloop()

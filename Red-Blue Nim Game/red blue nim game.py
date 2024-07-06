import customtkinter as ctk
from tkinter import messagebox


class RedBlueNimGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RED BLUE NIM GAME              MUHAMMAD UWAIM QURESHI")
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # lable for developer name
        self.lable_developer_name = ctk.CTkLabel(self.root,text="DEVELOPER: MUHAMMAD UWAIM QURESHI",font=("Arial",15))
        self.lable_developer_name.place(relx=0.8, rely=0.9, anchor="center")

        # lable for game name (blue red nim game)
        self.title_label = ctk.CTkLabel(self.root, text="RED BLUE NIM GAME", font=("Arial", 80))
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # red marbles
        self.red_label = ctk.CTkLabel(self.root, text="RED MARBLES: ", font=("Arial", 25))
        self.red_label.place(relx=0.2, rely=0.4, anchor="center")
        self.red_count = ctk.CTkLabel(self.root, text="0", font=("Arial", 25))
        self.red_count.place(relx=0.3, rely=0.4, anchor="center")

        # blue marbles
        self.blue_label = ctk.CTkLabel(self.root, text="BLUE MARBLES: ", font=("Arial", 25))
        self.blue_label.place(relx=0.5, rely=0.4, anchor="center")
        self.blue_count = ctk.CTkLabel(self.root, text="0", font=("Arial", 25))
        self.blue_count.place(relx=0.6, rely=0.4, anchor="center")

        # lable for score
        self.score_label = ctk.CTkLabel(self.root, text="SCORES: ", font=("Arial", 25))
        self.score_label.place(relx=0.3, rely=0.5, anchor="center")
        self.score_value = ctk.CTkLabel(self.root, text="HUMAN: 0, COMPUTER: 0", font=("Arial", 25))
        self.score_value.place(relx=0.44, rely=0.5, anchor="center")

        # lable for showing computer starts or human starts when user select on a player drop down
        self.message_label = ctk.CTkLabel(self.root, text="", font=("Arial", 30), wraplength=300)
        self.message_label.place(relx=0.8, rely=0.5, anchor="center")

        # lable for red marble removing
        self.red_move_label = ctk.CTkLabel(self.root, text="RED MARBLES TO REMOVE: ", font=("Arial", 25))
        self.red_move_label.place(relx=0.2, rely=0.6, anchor="center")
        self.red_move = ctk.CTkEntry(self.root, width=100, height=50, corner_radius=30, placeholder_text="",
                                     font=("Arial", 30))
        self.red_move.place(relx=0.4, rely=0.6, anchor="center")

        # lable for blue marble removing
        self.blue_move_label = ctk.CTkLabel(self.root, text="BLUE MARBLES TO REMOVE: ", font=("Arial", 25))
        self.blue_move_label.place(relx=0.2, rely=0.7, anchor="center")
        self.blue_move = ctk.CTkEntry(self.root, width=100, height=50, corner_radius=30, placeholder_text="",
                                      font=("Arial", 30))
        self.blue_move.place(relx=0.4, rely=0.7, anchor="center")

        # button for submission of moves
        self.submit_move_button = ctk.CTkButton(self.root, text="SUBMIT MOVES", command=self.human_move, width=400,
                                                height=70, font=("Arial", 30), corner_radius=30, fg_color="#000000",
                                                hover_color="#8B0000", border_width=2)
        self.submit_move_button.place(relx=0.4, rely=0.8, anchor="center")

        # game version drop down option
        self.version_label = ctk.CTkLabel(self.root, text="GAME VERSION: ", font=("Arial", 25))
        self.version_label.place(relx=0.55, rely=0.3, anchor="center")
        self.version_var = ctk.StringVar(value="STANDARD")
        self.version_menu = ctk.CTkOptionMenu(self.root, values=["STANDARD", "MISERE"], variable=self.version_var,
                                              width=250, height=50, corner_radius=25, font=("Arial", 25))
        self.version_menu.place(relx=0.77, rely=0.3, anchor="center")

        # player drop down option
        self.first_player_label = ctk.CTkLabel(self.root, text="FIRST PLAYER: ", font=("Arial", 25))
        self.first_player_label.place(relx=0.11, rely=0.3, anchor="center")
        self.first_player_var = ctk.StringVar(value="COMPUTER")
        self.first_player_menu = ctk.CTkOptionMenu(self.root, values=["COMPUTER", "HUMAN"],
                                                   variable=self.first_player_var, width=250, height=50,
                                                   corner_radius=25, font=("Arial", 25))
        self.first_player_menu.place(relx=0.33, rely=0.3, anchor="center")

        # button for start game
        self.start_button = ctk.CTkButton(self.root, text="START GAME", command=self.start_game, width=200, height=200,
                                          corner_radius=30, font=("Arial", 30), fg_color="#000000",
                                          hover_color="#8B0000", border_width=2)
        self.start_button.place(relx=0.8, rely=0.7, anchor="center")

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
    root.geometry("1366x768")
    root.mainloop()

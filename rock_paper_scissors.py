import random
from tkinter import *
from tkinter import messagebox
import tkinter.font as font

def rock_paper_scissors():
    def play_game():
        user_choice = user_var.get()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        result_text.set(f"The computer chose {computer_choice}.")

        if computer_choice == user_choice:
            result_text.set(result_text.get() + " It's a tie!")
            update_score("tie")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result_text.set(result_text.get() + " You win!")
            update_score("win")
        else:
            result_text.set(result_text.get() + " You lose!")
            update_score("loss")

    def update_score(outcome):
        if outcome == "win":
            scores["wins"] += 1
        elif outcome == "loss":
            scores["losses"] += 1
        else:
            scores["ties"] += 1

        score_label.config(text=f"Wins: {scores['wins']} | Losses: {scores['losses']} | Ties: {scores['ties']}")

    root = Tk()
    root.title("Rock Paper Scissors")
    root.geometry("500x600")
    root.resizable(0, 0)
    root.configure(bg="#333333")

    myFont = font.Font(family='Helvetica', size=20, weight='bold')

    label = Label(root, text="Choose your move:", fg="white", bg="#333333", font=myFont)
    label.place(relx=0.5, rely=0.1, anchor=CENTER)

    user_var = StringVar()
    choices = ["rock", "paper", "scissors"]
    user_choices = OptionMenu(root, user_var, *choices)
    user_choices.config(font=myFont, bg="green", fg="white", width=10)
    user_choices.place(relx=0.5, rely=0.2, anchor=CENTER)

    play_button = Button(root, text="Play", bg="green", fg="white", command=play_game)
    play_button['font'] = myFont
    play_button.place(relx=0.5, rely=0.35, anchor=CENTER)

    result_text = StringVar()
    result_label = Label(root, textvariable=result_text, fg="white", bg="#333333", font=myFont)
    result_label.place(relx=0.5, rely=0.45, anchor=CENTER)

    scores = {"wins": 0, "losses": 0, "ties": 0}
    score_label = Label(root, text="Wins: 0 | Losses: 0 | Ties: 0", fg="white", bg="#333333", font=myFont)
    score_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()

rock_paper_scissors()
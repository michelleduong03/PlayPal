import tkinter as tk
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import random
from tkinter import simpledialog, messagebox

def play_guess_number():
    number = random.randint(1, 100)
    tries = 0
    max_tries = 7

    while tries < max_tries:
        guess = custom_ask_integer(f"Try #{tries + 1}: Guess a number (1-100)")
        if guess is None:
            return # User cancelled
        tries += 1
        if guess == number:
            messagebox.showinfo("🎉 Yay!", f"You got it in {tries} tries!")
            return
        elif guess < number:
            messagebox.showinfo("Too Low", "Try a higher number!")
        else:
            messagebox.showinfo("Too High", "Try a lower number!")

    messagebox.showinfo("Game Over", f"Out of tries! The number was {number}.")

def custom_ask_integer(prompt):
    dialog = tk.Toplevel(app)
    dialog.title("Guess the Number")
    dialog.geometry("300x150")
    dialog.configure(bg="#2E2E2E") 
    dialog.grab_set()
    dialog.transient(app) 

    label = tk.Label(dialog, text=prompt, font=("Helvetica", 12), bg="#2E2E2E", fg="white")
    label.pack(pady=10)

    var = tk.StringVar()

    entry = tk.Entry(dialog, textvariable=var, font=("Helvetica", 14), bg="#3F3F3F", fg="white", insertbackground="white")
    entry.pack(pady=5)
    entry.focus_set()

    result = {'value': None}

    def on_ok():
        val = var.get()
        if val.isdigit():
            result['value'] = int(val)
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    def on_cancel():
        dialog.destroy()

    button_frame = tk.Frame(dialog, bg="#2E2E2E")
    button_frame.pack(pady=10)

    ok_button = tk.Button(button_frame, text="OK", command=on_ok, bg="#555555", fg="black", activebackground="#777777", activeforeground="white")
    ok_button.pack(side="left", padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel, bg="#555555", fg="black", activebackground="#777777", activeforeground="white")
    cancel_button.pack(side="left", padx=5)

    dialog.wait_window() 
    return result['value']

def play_rock_paper_scissors():
    choices = ['Rock', 'Paper', 'Scissors']
    rounds = 3
    user_score = 0
    comp_score = 0

    for i in range(1, rounds + 1):
        user_choice = custom_ask_choice(f"Round {i}: Choose Rock, Paper, or Scissors", choices)
        if user_choice is None:
            return  # User cancelled
        comp_choice = random.choice(choices)

        if user_choice == comp_choice:
            messagebox.showinfo("Tie!", f"Both chose {user_choice}. It's a tie!")
        elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
             (user_choice == 'Paper' and comp_choice == 'Rock') or \
             (user_choice == 'Scissors' and comp_choice == 'Paper'):
            user_score += 1
            messagebox.showinfo("You Win!", f"You chose {user_choice}, computer chose {comp_choice}. You win this round!")
        else:
            comp_score += 1
            messagebox.showinfo("You Lose!", f"You chose {user_choice}, computer chose {comp_choice}. You lose this round!")

    if user_score > comp_score:
        messagebox.showinfo("Game Over", f"You won! Score: {user_score} - {comp_score}")
    elif user_score < comp_score:
        messagebox.showinfo("Game Over", f"You lost! Score: {user_score} - {comp_score}")
    else:
        messagebox.showinfo("Game Over", f"It's a tie! Score: {user_score} - {comp_score}")

def custom_ask_choice(prompt, options):
    dialog = tk.Toplevel(app)
    dialog.title("Rock Paper Scissors")
    dialog.geometry("300x200")
    dialog.configure(bg="#2E2E2E")
    dialog.grab_set()
    dialog.transient(app)

    label = tk.Label(dialog, text=prompt, font=("Helvetica", 12), bg="#2E2E2E", fg="white")
    label.pack(pady=10)

    selected = {'value': None}

    def choose(option):
        selected['value'] = option
        dialog.destroy()

    for option in options:
        btn = tk.Button(dialog, text=option, font=("Helvetica", 14), 
                        bg="#555555", fg="black", activebackground="#777777", activeforeground="white",
                        command=lambda opt=option: choose(opt))
        btn.pack(fill='x', padx=30, pady=5)

    cancel_button = tk.Button(dialog, text="Cancel", font=("Helvetica", 14),
                              bg="#555555", fg="black", activebackground="#777777", activeforeground="white",
                              command=dialog.destroy)
    cancel_button.pack(pady=10)

    dialog.wait_window()
    return selected['value']

games = {
    "Guess the Number": play_guess_number,
    "Rock Paper Scissors": play_rock_paper_scissors,
    # "Tic Tac Toe": play_tic_tac_toe,
}

def spin_game():
    selected_game = random.choice(list(games.keys()))
    print(f"Spun: {selected_game}") 
    result_label.config(text=f"🎮 {selected_game}") 
    result_label.update_idletasks() 
    play_button.config(state="normal", command=games[selected_game]) 

app = tk.Tk()
app.title("Random Game Generator")
app.geometry("400x300")
app.configure(bg="#2E2E2E")

app.lift()
app.attributes('-topmost', True)
app.after_idle(app.attributes, '-topmost', False)

# Main title
title = tk.Label(app, text="🎲 What Game Should I Play?", font=("Helvetica", 16, "bold"), bg="#2E2E2E", fg="white")
title.pack(pady=20)

# Spin button
spin_button = tk.Button(app, text="Spin!", font=("Helvetica", 14), command=spin_game, fg="black", bg="#555555", activebackground="#777777", activeforeground="white")
spin_button.pack(pady=10)

# Result label (now with initial text!)
result_label = tk.Label(app, text="Click 'Spin!' to choose a game!", font=("Helvetica", 14), bg="#2E2E2E", fg="white")
result_label.pack(pady=10)

# Play button (initially disabled)
play_button = tk.Button(app, text="Play", font=("Helvetica", 14), state="disabled", fg="black", bg="#555555", activebackground="#777777", activeforeground="white")
play_button.pack(pady=10)

print("Launching app...")
app.mainloop()

import tkinter as tk
import random

number = random.randint(1, 100)

def check_guess():
    guess = int(entry.get())

    if guess < number:
        result.config(text="Too low! Try again.")
    elif guess > number:
        result.config(text="Too high! Try again.")
    else:
        result.config(text="correct! You guessed it!")

window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("350x250")

title = tk.Label(window, text="Guess a Number (1-100)")
title.pack(pady=20)

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="check Guess", command=check_guess)
button.pack(pady=15)

result = tk.Label(window, text="")
result.pack()

window.mainloop()

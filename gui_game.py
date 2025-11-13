import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

        # Slightly larger window for spacing
        self.root.geometry("350x220")

        # generate the secret number
        self.number = random.randint(1, 20)
        self.attempts = 0

        # top label with slightly more padding
        tk.Label(root, text="I'm thinking of a number between 1 and 20").pack(pady=15)

        # input field with placeholder text
        self.entry = tk.Entry(root)
        self.entry.insert(0, "Enter a number...")
        self.entry.pack(pady=5)

        tk.Button(root, text="Guess", command=self.check_guess).pack(pady=5)

        self.result = tk.Label(root, text="", fg="blue")
        self.result.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.number:
                self.result.config(text="Too low! Try again.")
            elif guess > self.number:
                self.result.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Result", f"You got it in {self.attempts} attempts!")
                self.root.destroy()
        except ValueError:
            messagebox.showwarning("Error", "Please enter a number!")

if __name__ == "__main__":
    root = tk.Tk()
    GuessingGame(root)
    root.mainloop()

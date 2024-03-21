import tkinter as tk
from tkinter import messagebox
import random

# Constants for the number range and maximum allowed guesses
MIN_RANGE = 1
MAX_RANGE = 200
MAX_GUESSES = 6

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.title("Number Guessing Game")
        self.geometry("400x200")

        # Initialize game variables
        self.number_to_guess = random.randint(MIN_RANGE, MAX_RANGE)
        self.guess_count = 0

        # Create and pack the initial label and entry for the player's name
        self.label = tk.Label(self, text="May I ask you for your name?")
        self.label.pack(pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=10)

        # Create and pack the button to start the game
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game, width=13, font=("arial", "10"), bg='#83E0F2')
        self.start_button.pack(pady=10)

    def start_game(self):
        # Get the player's name and reset game variables
        self.player_name = self.name_entry.get()
        self.guess_count = 0
        self.number_to_guess = random.randint(MIN_RANGE, MAX_RANGE)

        # Update label, hide name entry and start button, and show guess entry
        self.label.config(text=f"{self.player_name}, I am thinking of a number between {MIN_RANGE} and {MAX_RANGE}")
        self.name_entry.pack_forget()
        self.start_button.pack_forget()

        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack(pady=10)

        # Create and pack the button to submit guesses
        self.submit_button = tk.Button(self, text="Submit Guess", command=self.make_guess, width=13, font=("arial", "10"), bg='#83E0F2')
        self.submit_button.pack(pady=10)

    def make_guess(self):
        try:
            # Get the player's guess and increment the guess count
            guess = int(self.guess_entry.get())
            self.guess_count += 1

            # Check if the guess is within the valid range
            if MIN_RANGE <= guess <= MAX_RANGE:
                # Compare the guess with the random number
                if guess < self.number_to_guess:
                    messagebox.showinfo("Result", "Too low. Try again!")
                elif guess > self.number_to_guess:
                    messagebox.showinfo("Result", "Too high. Try again!")
                else:
                    messagebox.showinfo("Congratulations", f"Good job, {self.player_name}! You guessed my number in {self.guess_count} guesses!")
                    self.restart_game()
                    return

                # Check if the player has more guesses left
                if self.guess_count < MAX_GUESSES:
                    self.guess_entry.delete(0, tk.END)
                else:
                    messagebox.showinfo("Game Over", f"Nope. The number I was thinking of was {self.number_to_guess}")
                    self.restart_game()
            else:
                messagebox.showerror("Invalid Input", f"Please enter a number between {MIN_RANGE} and {MAX_RANGE}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def restart_game(self):
        # Hide guess entry and submit button, show name entry and start button
        self.guess_entry.pack_forget()
        self.submit_button.pack_forget()

        self.name_entry.delete(0, tk.END)
        self.name_entry.pack(pady=10)

        self.start_button.pack(pady=10)

# Run the application if the script is executed
if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()

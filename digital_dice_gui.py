#Add a GUI with tkinter

import random
import tkinter as tk

def roll_dice():
    dice_value = random.randint(1, 6)
    result_label.config(text=f"Dice rolled: {dice_value}")

# Set up the main application window
root = tk.Tk()
root.title("Digital Dice")

# Add a label to display the result
result_label = tk.Label(root, text="Press Roll to start", font=("Helvetica", 24))
result_label.pack(pady=20)

# Add a button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Helvetica", 18))
roll_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()



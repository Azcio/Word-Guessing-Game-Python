import tkinter as tk
from src.app import wordSelector, display_progress

# --- Setup main window ---
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("700x800")  # extra height for buttons

# --- Game state variables ---
word = None
guessed_letters = ""
attempts = 5
char_boxes = []
current_row = 0
current_col = 0

# --- Widgets ---
label = tk.Label(root, text="", font=("Helvetica", 24))
label.pack(pady=20)

box_frame = tk.Frame(root)
box_frame.pack(pady=20)

message_label = tk.Label(root, text="", font=("Helvetica", 20))
message_label.pack(pady=20)

# --- Functions ---
def start_game():
    """Initialize or restart the game."""
    global word, guessed_letters, char_boxes, current_row, current_col
    word = wordSelector()
    guessed_letters = ""
    current_row = 0
    current_col = 0
    char_boxes = []

    # Reset progress text
    label.config(text=display_progress(word, guessed_letters))

    # Clear box frame
    for widget in box_frame.winfo_children():
        widget.destroy()

    # Create new grid
    for row in range(attempts):
        row_boxes = []
        for col in range(len(word)):
            box = tk.Label(box_frame, text="_", width=4, height=2,
                           borderwidth=2, relief="solid", font=("Arial", 24), bg="white")
            box.grid(row=row, column=col, padx=5, pady=5)
            row_boxes.append(box)
        char_boxes.append(row_boxes)

    # Clear message label
    message_label.config(text="", fg="black")

def handle_keypress(event):
    """Handle user typing letters into the grid."""
    global current_row, current_col

    if current_row >= attempts:
        return  # no more rows left

    char = event.char.lower()

    if char.isalpha() and current_col < len(word):
        char_boxes[current_row][current_col].config(text=char.upper())
        current_col += 1

    elif event.keysym == "BackSpace" and current_col > 0:
        current_col -= 1
        char_boxes[current_row][current_col].config(text="_")

    elif event.keysym == "Return" and current_col == len(word):
        guess = "".join(box.cget("text").lower() for box in char_boxes[current_row])

        # Color feedback
        for col, ch in enumerate(guess):
            if ch == word[col]:
                char_boxes[current_row][col].config(bg="green")
            elif ch in word:
                char_boxes[current_row][col].config(bg="yellow")
            else:
                char_boxes[current_row][col].config(bg="gray")

        # Check win condition
        if guess == word:
            message_label.config(text="🎉 You Win!", fg="green")
            return

        # Next row
        current_row += 1
        current_col = 0

        # Check lose condition
        if current_row == attempts:
            message_label.config(text=f"❌ You Lose! Word was: {word}", fg="red")

# --- Buttons ---
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

restart_button = tk.Button(button_frame, text="🔄 Restart", font=("Arial", 14),
                           command=start_game)
restart_button.grid(row=0, column=0, padx=10)

quit_button = tk.Button(button_frame, text="❌ Quit", font=("Arial", 14),
                        command=root.destroy)
quit_button.grid(row=0, column=1, padx=10)

# --- Bind keys & start game ---
root.bind("<Key>", handle_keypress)
start_game()

# --- Run GUI ---
root.mainloop()

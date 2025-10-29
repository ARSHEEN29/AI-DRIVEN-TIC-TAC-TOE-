import tkinter as tk
from tkinter import messagebox

# -------------------------------------------------------
#  🎮 TIC TAC TOE - Creative Knowledge-Based AI (Tkinter)
# -------------------------------------------------------

board = [" " for _ in range(9)]
buttons = []

# -----------------------------
# Logic for winner & AI move
# -----------------------------
def check_winner(symbol):
    combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] == symbol:
            return (True, (a,b,c))
    return (False, None)

def knowledge_based_move():
    # Rule 1: Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            won, _ = check_winner("X")
            if won: return
            board[i] = " "
    # Rule 2: Block opponent
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            won, _ = check_winner("O")
            if won:
                board[i] = "X"
                return
            board[i] = " "
    # Rule 3: Pick first empty
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            return

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("✨ Tic Tac Toe - Knowledge Based AI ✨")
root.geometry("500x600")
root.config(bg="#1E1E2E")

status_text = tk.StringVar()
status_text.set("💡 Your Turn (You: O | AI: X)")

# Header
title = tk.Label(root, text="TIC TAC TOE", font=("Comic Sans MS", 26, "bold"),
                 bg="#1E1E2E", fg="#F8BD96")
title.pack(pady=10)

status_label = tk.Label(root, textvariable=status_text,
                        font=("Comic Sans MS", 16, "italic"),
                        bg="#1E1E2E", fg="#ABE9B3")
status_label.pack(pady=10)

# Board Frame
frame = tk.Frame(root, bg="#1E1E2E")
frame.pack(pady=20)

def highlight_winner(combo, symbol):
    for i in combo:
        buttons[i].config(bg="#F5C2E7" if symbol == "O" else "#89B4FA")
    status_text.set(f"🏆 { 'You Win!' if symbol == 'O' else 'AI Wins!' }")
    for b in buttons:
        b.config(state="disabled")

def handle_click(i):
    if board[i] == " ":
        board[i] = "O"
        buttons[i].config(text="O", fg="#F28FAD", bg="#F8E1E1")
        won, combo = check_winner("O")
        if won:
            highlight_winner(combo, "O")
            return
        if " " not in board:
            status_text.set("🤝 It's a Draw!")
            return
        
        # AI Move
        knowledge_based_move()
        for j in range(9):
            if board[j] == "X" and buttons[j]["text"] == " ":
                buttons[j].config(text="X", fg="#89B4FA", bg="#DCE7FA")
        won, combo = check_winner("X")
        if won:
            highlight_winner(combo, "X")
            return
        if " " not in board:
            status_text.set("🤝 It's a Draw!")

def reset_game():
    global board
    board = [" " for _ in range(9)]
    status_text.set("💡 Your Turn (You: O | AI: X)")
    for btn in buttons:
        btn.config(text=" ", bg="#C3BAC6", state="normal")

# Create Buttons
for i in range(9):
    btn = tk.Button(frame, text=" ", font=("Comic Sans MS", 32, "bold"),
                    width=3, height=1, bg="#C3BAC6", fg="white",
                    activebackground="#F38BA8", relief="raised",
                    command=lambda i=i: handle_click(i))
    btn.grid(row=i//3, column=i%3, padx=10, pady=10)
    buttons.append(btn)

# Reset Button
reset_btn = tk.Button(root, text="🔄 Restart Game", font=("Comic Sans MS", 14, "bold"),
                      bg="#A6E3A1", fg="#1E1E2E", activebackground="#B5E8E0",
                      relief="ridge", padx=10, pady=5, command=reset_game)
reset_btn.pack(pady=15)

# Footer
footer = tk.Label(root, text="🧠 Knowledge-Based AI | Designed by Arshee",
                  font=("Comic Sans MS", 10, "italic"),
                  bg="#1E1E2E", fg="#B4BEFE")
footer.pack(side="bottom", pady=10)

root.mainloop()

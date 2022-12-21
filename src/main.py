import tkinter as tk

root = tk.Tk()
root.title("Horde Chess")

# Create the canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

square_size = 50

# Draw the board
for row in range(8):
    for col in range(8):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        color = "white" if (row + col) % 2 == 0 else "black"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# Draw a white piece
x = 2 * square_size
y = 6 * square_size
piece = canvas.create_oval(x + 10, y + 10, x + 40, y + 40, fill="white")

# Event handlers
selected_piece = None

def on_piece_press(event):
    global selected_piece
    x, y = event.x, event.y
    selected_piece = canvas.find_withtag("current")[0]

def on_piece_drag(event):
    x, y = event.x, event.y
    canvas.coords(selected_piece, x - square_size / 2, y - square_size / 2,
                         x + square_size / 2, y + square_size / 2)

def on_piece_release(event):
    global selected_piece
    x, y = event.x, event.y
    canvas.coords(selected_piece, x - square_size / 2, y - square_size / 2,
                         x + square_size / 2, y + square_size / 2)
    selected_piece = None

# Bind events to the canvas
canvas.bind_all("<Button-1>", on_piece_press)
canvas.bind_all("<B1-Motion>", on_piece_drag)
canvas.bind_all("<ButtonRelease-1>", on_piece_release)

# Create color select buttons
color = tk.StringVar()

white_button = tk.Radiobutton(root, text="White", variable=color, value="white")
white_button.pack()

black_button = tk.Radiobutton(root, text="Black", variable=color, value="black")
black_button.pack()

# To get the chosen color, use `color.get()`

root.mainloop()

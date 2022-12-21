import tkinter as tk

window = tk.Tk()
window.title("Chess Board")
canvas = tk.Canvas(window, width=8*60, height=8*60)
canvas.pack()

def draw_board(square_size = 60):
    # clear the canvas
    canvas.delete("all")
# draw the squares of the board
    for i in range(8):
        for j in range(8):
            x1 = i * square_size
            y1 = j * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            color = 'white' if (i+j) % 2 == 0 else 'silver'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

draw_board()

window.mainloop()
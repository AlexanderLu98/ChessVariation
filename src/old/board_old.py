import tkinter as tk

# define the size of each square on the board
SQUARE_SIZE = 50

# create the window
window = tk.Tk()
window.title("Chess Board")

# create a canvas to draw the board on
canvas = tk.Canvas(window, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
canvas.pack()

# draw the squares of the board
for i in range(8):
    for j in range(8):
        x1 = i * SQUARE_SIZE
        y1 = j * SQUARE_SIZE
        x2 = x1 + SQUARE_SIZE
        y2 = y1 + SQUARE_SIZE
        color = 'white' if (i+j) % 2 == 0 else 'black'
        square = canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# draw the vertical and horizontal lines for the coordinates
for i in range(9):
    x = i * SQUARE_SIZE
    # draw the vertical lines
    canvas.create_line(x, 0, x, 8*SQUARE_SIZE, width=2)
    # add the labels for the vertical coordinates
    if i > 0:
        label = tk.Label(canvas, text=f"{chr(ord('a') + i - 1)}")
        canvas.create_window(x + SQUARE_SIZE/2, -SQUARE_SIZE/2, window=label)
for i in range(9):
    y = i * SQUARE_SIZE
    # draw the horizontal lines
    canvas.create_line(0, y, 8*SQUARE_SIZE, y, width=2)
    # add the labels for the horizontal coordinates
    if i < 8:
        label = tk.Label(canvas, text=f"{8 - i}")
        canvas.create_window(-SQUARE_SIZE/2, y + SQUARE_SIZE/2, window=label)


# start the event loop
window.mainloop()

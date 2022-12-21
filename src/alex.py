import tkinter as tk

SQUARE_SIZE = 60

window = tk.Tk()
window.title("Chess Board")

# create a canvas to draw the board on
canvas = tk.Canvas(window, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
canvas.pack()

for i in range(8):
        for j in range(8):
            x1 = i * SQUARE_SIZE
            y1 = j * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            color = 'white' if (i+j) % 2 == 0 else 'lightgrey'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)


white_rook_img = tk.PhotoImage(file='src\images\Rook_white.png')
canvas.create_image(0, 0, image=white_rook_img, anchor='center')

window.mainloop()
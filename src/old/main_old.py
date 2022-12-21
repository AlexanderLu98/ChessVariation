import tkinter as tk

def move_piece(from_x, from_y, to_x, to_y):
    # update the positions list with the new position of the piece
    positions[to_y][to_x], positions[from_y][from_x] = positions[from_y][from_x], positions[to_y][to_x]
    # redraw the board with the updated positions
    draw_board()

# function to handle when a piece is clicked
def on_piece_click(event):
    global from_x, from_y, to_x, to_y
    # get the coordinates of the click event
    to_x, to_y = (event.x // SQUARE_SIZE), (event.y // SQUARE_SIZE)
    # check if a piece is already selected
    if from_x is not None and from_y is not None:
        # move the piece
        move_piece(from_x, from_y, to_x, to_y)
        # reset the from coordinates
        from_x = None
        from_y = None
    else:
        # select the piece to be moved
        from_x, from_y = to_x, to_y


# define the size of each square on the board
SQUARE_SIZE = 60

# create the window
window = tk.Tk()
window.title("Chess Board")

# create a canvas to draw the board on
canvas = tk.Canvas(window, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
canvas.pack()

# define the positions of the pieces
positions = [
    ('R', 0, 7), ('N', 1, 7), ('B', 2, 7), ('Q', 3, 7), ('K', 4, 7), ('B2', 5, 7), ('N2', 6, 7), ('R2', 7, 7),
    ('P', 0, 6), ('P2', 1, 6), ('P3', 2, 6), ('P4', 3, 6), ('P5', 4, 6), ('P6', 5, 6), ('P7', 6, 6), ('P8', 7, 6),
    (' ', 0, 5), (' ', 1, 5), (' ', 2, 5), (' ', 3, 5), (' ', 4, 5), (' ', 5, 5), (' ', 6, 5), (' ', 7, 5),
    (' ', 0, 4), (' ', 1, 4), (' ', 2, 4), (' ', 3, 4), (' ', 4, 4), (' ', 5, 4), (' ', 6, 4), (' ', 7, 4),
    (' ', 0, 3), (' ', 1, 3), (' ', 2, 3), (' ', 3, 3), (' ', 4, 3), (' ', 5, 3), (' ', 6, 3), (' ', 7, 3),
    (' ', 0, 2), (' ', 1, 2), (' ', 2, 2), (' ', 3, 2), (' ', 4, 2), (' ', 5, 2), (' ', 6, 2), (' ', 7, 2),
    ('p', 0, 1), ('p2', 1, 1), ('p3', 2, 1), ('p4', 3, 1), ('p5', 4, 1), ('p6', 5, 1), ('p7', 6, 1), ('p8', 7, 1),
    ('r', 0, 0), ('n', 1, 0), ('b', 2, 0), ('q', 3, 0), ('k', 4, 0), ('b2', 5, 0), ('n2', 6, 0), ('r2', 7, 0)
]
# create global variables to track the position of the piece being moved
from_x = None
from_y = None
to_x = None
to_y = None

def draw_board():
    # clear the canvas
    canvas.delete("all")
# draw the squares of the board
    for i in range(8):
        for j in range(8):
            x1 = i * SQUARE_SIZE
            y1 = j * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            color = 'white' if (i+j) % 2 == 0 else 'lightgrey'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# create the pieces
    for piece, i, j in positions:
        x = i * SQUARE_SIZE + SQUARE_SIZE // 2
        y = j * SQUARE_SIZE + SQUARE_SIZE // 2

        if piece == 'R':
            white_rook_img = tk.PhotoImage(file='src\images\Rook_white.png')
            canvas.create_image(x, y, image=white_rook_img, anchor='center')
        elif piece == 'N':
            white_knight_img = tk.PhotoImage(file='src\images\knight_white.png')
            canvas.create_image(x, y, image=white_knight_img, anchor='center')
        elif piece == 'B':
            white_bishop_img = tk.PhotoImage(file='src\images\Bishop_white.png')
            canvas.create_image(x, y, image=white_bishop_img, anchor='center')
        if piece == 'R2':
            white_rook2_img = tk.PhotoImage(file='src\images\Rook_white.png')
            canvas.create_image(x, y, image=white_rook2_img, anchor='center')
        elif piece == 'N2':
            white_knight2_img = tk.PhotoImage(file='src\images\knight_white.png')
            canvas.create_image(x, y, image=white_knight2_img, anchor='center')
        elif piece == 'B2':
            white_bishop2_img = tk.PhotoImage(file='src\images\Bishop_white.png')
            canvas.create_image(x, y, image=white_bishop2_img, anchor='center')
        elif piece == 'Q':
            white_queen_img = tk.PhotoImage(file='src\images\queen_white.png')
            canvas.create_image(x, y, image=white_queen_img, anchor='center')
        elif piece == 'K':
            white_king_img = tk.PhotoImage(file='src\images\king_white.png')
            canvas.create_image(x, y, image=white_king_img, anchor='center')
        elif piece == 'P':
            white_pawn_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn_img, anchor='center')
        elif piece == 'P2':
            white_pawn2_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn2_img, anchor='center')
        elif piece == 'P3':
            white_pawn3_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn3_img, anchor='center')
        elif piece == 'P4':
            white_pawn4_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn4_img, anchor='center')
        elif piece == 'P5':
            white_pawn5_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn5_img, anchor='center')
        elif piece == 'P6':
            white_pawn6_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn6_img, anchor='center')
        elif piece == 'P7':
            white_pawn7_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn7_img, anchor='center')
        elif piece == 'P8':
            white_pawn8_img = tk.PhotoImage(file='src\images\pawn_white.png')
            canvas.create_image(x, y, image=white_pawn8_img, anchor='center')
        elif piece == 'p':
            pawn_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn_img, anchor='center')
        elif piece == 'p2':
            pawn2_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn2_img, anchor='center')
        elif piece == 'p3':
            pawn3_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn3_img, anchor='center')
        elif piece == 'p4':
            pawn4_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn4_img, anchor='center')
        elif piece == 'p5':
            pawn5_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn5_img, anchor='center')
        elif piece == 'p6':
            pawn6_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn6_img, anchor='center')
        elif piece == 'p7':
            pawn7_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn7_img, anchor='center')
        elif piece == 'p8':
            pawn8_img = tk.PhotoImage(file='src\images\pawn_black.png')
            canvas.create_image(x, y, image=pawn8_img, anchor='center')
        elif piece == 'r':
            rook_img = tk.PhotoImage(file='src\images\Rook_black.png')
            canvas.create_image(x, y, image=rook_img, anchor='center')
        elif piece == 'n':
            knight_img = tk.PhotoImage(file='src\images\knight_black.png')
            canvas.create_image(x, y, image=knight_img, anchor='center')
        elif piece == 'b':
            bishop_img = tk.PhotoImage(file='src\images\Bishop_black.png')
            canvas.create_image(x, y, image=bishop_img, anchor='center')
        elif piece == 'r2':
            rook2_img = tk.PhotoImage(file='src\images\Rook_black.png')
            canvas.create_image(x, y, image=rook2_img, anchor='center')
        elif piece == 'n2':
            knight2_img = tk.PhotoImage(file='src\images\knight_black.png')
            canvas.create_image(x, y, image=knight2_img, anchor='center')
        elif piece == 'b2':
            bishop2_img = tk.PhotoImage(file='src\images\Bishop_black.png')
            canvas.create_image(x, y, image=bishop2_img, anchor='center')
        elif piece == 'q':
            queen_img = tk.PhotoImage(file='src\images\queen_black.png')
            canvas.create_image(x, y, image=queen_img, anchor='center')
        elif piece == 'k':
            king_img = tk.PhotoImage(file='src\images\king_black.png')
            canvas.create_image(x, y, image=king_img, anchor='center')
    
draw_board()
# bind an event to the canvas to detect when a piece is clicked
canvas.bind("<Button-1>", on_piece_click)

# start the event loop
window.mainloop()

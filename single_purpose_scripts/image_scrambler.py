from PIL import Image

# Load input
puzzle = Image.open("test2.png")
width, height = puzzle.size
# And initialize new image
solution = Image.new(mode = "RGBA", size = puzzle.size)

# Get width and height for each piece
piece_width = width // 4
piece_height = height // 4

# Loop through each row, then each column
row_counter = 0
for row in range(0, height, piece_height):
    col_counter = 0
    
    for col in range(0, width, piece_width):
        left = col
        top = row
        right = left + piece_width
        bottom = top + piece_height
        
        # Top x, top y, top x, bottom y    
        box = (left, top, right, bottom)
        # Get piece from original
        piece = puzzle.crop(box)
        # Paste piece
        # Piece at row 0, col 2 is pasted at row 2, col 0 
        x_paste = row_counter * piece_width
        y_paste = col_counter * piece_height
        
        solution.paste(piece, (x_paste, y_paste))
        
        col_counter += 1
        
    row_counter += 1

solution.save("out2.png")
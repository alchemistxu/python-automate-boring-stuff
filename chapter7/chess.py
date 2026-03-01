import sys, copy

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bp', 'b7': 'bp',
'c7': 'bp', 'd7': 'bp', 'e7': 'bp', 'f7': 'bp', 'g7': 'bp', 'h7': 'bp',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wp', 'b2': 'wp', 'c2': 'wp', 'd2': 'wp',
'e2': 'wp', 'f2': 'wp', 'g2': 'wp', 'h2': 'wp'}

BOARD_TEMPLATE = '''
      a    b   c     d   e    f    g     h
    ---- ---- ---- ---- ---- ---- ---- ----
   ||||||    ||||||    ||||||    ||||||    |  
 8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
   ||||||    ||||||    ||||||    ||||||    |
   |    ||||||    ||||||    ||||||    |||||| 
 7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
   |----||||||----||||||----||||||----||||||
   ||||||    ||||||    ||||||    ||||||    |  
 6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
   ||||||    ||||||    ||||||    ||||||    |
   |    ||||||    ||||||    ||||||    |||||| 
 5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
   |----||||||----||||||----||||||----||||||
   ||||||    ||||||    ||||||    ||||||    |  
 4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
   ||||||    ||||||    ||||||    ||||||    |
   |    ||||||    ||||||    ||||||    |||||| 
 3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
   |----||||||----||||||----||||||----||||||
   ||||||    ||||||    ||||||    ||||||    |  
 2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
   ||||||    ||||||    ||||||    ||||||    |
   |    ||||||    ||||||    ||||||    |||||| 
 1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
   |----||||||----||||||----||||||----||||||
'''

WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

def print_chessboard(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            if x + y in board.keys():
                squares.append(board[x + y])
            else:
                if is_white_square:
                    squares.append(WHITE_SQUARE)
                else:
                    squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square
    print(BOARD_TEMPLATE.format(*squares))  # get values in squares

CHESS_BOARD = '''
Interactive Chessboard
    w - White, b - Black'
    P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King'
Commands:'
    move e2 e4  - Moves the piece at e2 to e4'
    remove e2   - Removes the piece at e2'
    set e2 wP   - Sets square e2 to a white pawn'
    reset       - Resets pieces back to their starting squares'
    clear       - Clears the entire board'
    fill wP     - Fills entire board with white pawns.'
    quit        - Quits the program'
'''

print(CHESS_BOARD)
#print_chessboard(STARTING_PIECES)
main_board = copy.copy(STARTING_PIECES)
while True:
    print_chessboard(main_board)
    response = input('>').split()
    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == 'remove':
        del main_board[response[1]]
    elif response[0] == 'set':
        main_board[response[1]] = response[2]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {}
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x+y] = response[1]
    elif response[0] == 'quit':
        sys.exit()

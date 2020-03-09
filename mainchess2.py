"""
Python program to model the Chess piece position
in the Chess board
"""

EMPTY_SQUARE = " "
 
class Model(object):
    def __init__(self):
        '''create a chess board with pieces positioned for a new game
        row ordering is reversed from normal chess representations
        but corresponds to a top left screen coordinate 
        '''
         
        self.board = []
        pawn_base = "P "*8
        white_pieces =  "R N B Q K B N R"
        white_pawns = pawn_base.strip() 
        black_pieces = white_pieces.lower()
        black_pawns = white_pawns.lower()
        self.board.append(black_pieces.split(" "))
        self.board.append(black_pawns.split(" "))
        for i in range(4):
            self.board.append([EMPTY_SQUARE]*8)
        self.board.append(white_pawns.split(" "))
        self.board.append(white_pieces.split(" "))


# Making instances of model and its attribute board
# which represent a chess board

column_reference = "a b c d e f g h".split(" ")
class View(object):
    def __init__(self):
        pass
    def display(self,  board):
        print("%s: %s"%(" ", column_reference))
        print("-"*50)
        for i, row in enumerate(board):
            row_marker = 8-i
            print("%s: %s"%(row_marker,  row))


#column_reference = "1 2 3 4 5 6 7 8".split(" ")
column_reference = "a b c d e f g h".split(" ")
EMPTY_SQUARE = " "
 
class Model(object):
    def __init__(self):
        '''create a chess board with pieces positioned for a new game
        row ordering is reversed from normal chess representations
        but corresponds to a top left screen coordinate 
        '''
         
        self.board = []
        pawn_base = "P "*8
        white_pieces =  "R N B Q K B N R"
        white_pawns = pawn_base.strip() 
        black_pieces = white_pieces.lower()
        black_pawns = white_pawns.lower()
        self.board.append(black_pieces.split(" "))
        self.board.append(black_pawns.split(" "))
        for i in range(4):
            self.board.append([EMPTY_SQUARE]*8)
        self.board.append(white_pawns.split(" "))
        self.board.append(white_pieces.split(" "))
 
    def move(self, start,  destination):
        ''' move a piece located at the start location to destination
        (each an instance of BoardLocation)
        Does not check whether the move is valid for the piece
        '''
        # error checking
        for c in [start, destination]:  # check coordinates are valid
            if c.i > 7 or c.j > 7 or c.i <0 or c.j <0:
                return
        if start.i == destination.i and start.j == destination.j: # don't move to same location
            return
 
        if self.board[start.i][start.j] == EMPTY_SQUARE:  #nothing to move
            return
             
        f = self.board[start.i][start.j]
        self.board[destination.i][destination.j] = f
        self.board[start.i][start.j] = EMPTY_SQUARE
 
 
class BoardLocation(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
         
 
class View(object):
    def __init__(self):
        pass
    def display(self,  board):
        print("%s: %s"%(" ", column_reference))
        print("-"*50)
        for i, row in enumerate(board):
            row_marker = 8-i
            print("%s: %s"%(row_marker,  row))
         
 
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
     
    def run(self):
        ''' main loop'''
        while True:
            self.view.display(self.model.board)
            move = input("move (eg e2-e4) ")
            move = move.lower()
            if move =="q":
                break
            if move =="":
                move = "e2-e4"
            start,  destination = self.parse_move(move)
            self.model.move(start, destination)
             
    def parse_move(self, move):
        ''' Very basic move parsing 
        given a move in the form ab-cd where a and c are in [a,b,c,d,e,f,g,h]
        and b and d are numbers from 1 to 8 convert into BoardLocation instances
        for start (ab) and destination (cd)
        Does not deal with castling (ie 0-0 or 0-0-0) or bare pawn moves (e4)
        or capture d4xe5 etc
        No error checking! very fragile
        '''
         
        s, d = move.split("-")
 
        i = 8- int(s[-1]) # board is "upside down" with reference to the representation
        j = column_reference.index(s[0])
        start = BoardLocation(i, j)
         
        i =  8- int(d[-1])
        j= column_reference.index(d[0])
        destination = BoardLocation(i, j)
 
        return start,  destination
         
 
if __name__=="__main__":
    C = Controller()
    C.run()



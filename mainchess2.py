"""
Python program to model the Chess piece position
in the Chess board
"""

EMPTY_SQUARE = " "
 
class Model(object):
    def __init__(self):
        '''create a chess board with pieces positioned  
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
        """create a chess board with pieces positioned 
        row by column ordering
        """
         
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
 
    def move(self, begin,  dest):
        ''' move a piece located at the start location to destination
        '''
        # sanity checking
        for c in [begin, dest]:  # check coordinates are valid
            if c.i > 7 or c.j > 7 or c.i <0 or c.j <0:
                return
        if begin.i == dest.i and begin.j == dest.j: # don't move to same location
            return
 
        if self.board[begin.i][begin.j] == EMPTY_SQUARE:  #nothing to move
            return
             
        f = self.board[begin.i][begin.j]
        self.board[dest.i][dest.j] = f
        self.board[begin.i][begin.j] = EMPTY_SQUARE
 
 
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
         
 # Modelling the view of the board
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
        ''' 
        Major basic move parsing if
        given a move in the form ab-cd where a and c are in [a,b,c,d,e,f,g,h]
      
        '''
         
        s, d = move.split("-")
 
        i = 8- int(s[-1]) # board is "upside down" with reference to the representation
        j = column_reference.index(s[0])
        start = BoardLocation(i, j)
         
        i =  8- int(d[-1])
        j= column_reference.index(d[0])
        destination = BoardLocation(i, j)
 
        return start,  destination
         
# Testing the code
if __name__=="__main__":
    C = Controller()
    C.run()



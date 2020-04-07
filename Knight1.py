"""
Program to illustrate that count the number of moves Knight makes
in a Trio Chess Board if given a three player chess numbers.
"""
# Python3 program to find number 
# of possible moves of knight 
n = 4; 
m = 4;
l = 4;
  
# To calculate possible moves 
def KnightPossibleMoves(mat, p, q, d): 
    global n, m ,l; 
      
    # All possible moves of a knight 
    X = [2, 0, -1, -2, -2, -1, 1, 2]; 
    Y = [1, 2, 2, 0, -1, -2, -2, -1];
    P = [-1, 0, 1, -2, 2, -1, 1, 0];
  
    count = 0; 
  
    # Check if each possible move 
    # is valid or not 
    for i in range(8): 
          
        # Position of knight after move 
        x = p + X[i]; 
        y = q + Y[i];
        t = d + P[i];
  
        # count valid moves 
        if(x >= 0 and y >= 0 and t >= 0 and x < n and
           y < m and t < l ):# and mat[x][y][t] == 0): 
            count += 1; 
  
    # Return number of possible moves 
    return count; 
  
# Driver code 
if __name__ == '__main__': 
    mat = [[1, 0, 1, 0], [0, 1, 1, 1],  
           [1, 1, 0, 1], [0, 1, 1, 1],
           [0, 1, 0, 1], [0, 1, 1, 1]]; 
  
    #p, q, d = 1, 1, 1;
    #p, q, d = 2, 2, 2; # No. of moves 3
    #p, q, d = 4, 4, 4;
    p, q, d = 1, 3, 1;
    #p, q, d = 2, 3, 2; # No. of moves 3
    
    
  
    print(KnightPossibleMoves(mat, p, q, d)); 

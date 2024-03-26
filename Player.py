from Board.py import Board

# write your class below.

class Player:
    
    def __init__(self, checker):
        """ constructs a new Player object
        """
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
        
    
    def __repr__(self):
        """ method that returns a string representing a Player object
        """
        player = str('Player ' + self.checker)
        return player
    
    
    def opponent_checker(self):
        """ method that returns a one-character string representing the 
            checker of the Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        elif self.checker == 'O':
            return 'X'
        
        
    def next_move(self, b):
        """ method that accepts a Board object b as a parameter and returns 
            the column where the player wants to make the next move
        """
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')
        

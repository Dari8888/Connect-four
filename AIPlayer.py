import random  
from Game import *

class AIPlayer(Player):
    """  will look ahead some number of moves into the future to assess the 
        impact of each possible move that it could make for its next move, 
        and it will assign a score to each possible move
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """ method that returns a string representing an AIPlayer object
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + \
               str(self.lookahead) + ')'
               
               
    def max_score_column(self, scores):
        """ method that takes a list scores containing a score for each 
            column of the board, and that returns the index of the column 
            with the maximum score
        """
        max_score = max(scores)
        index = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                index += [i]
        if self.tiebreak == 'RIGHT':
            return index[-1]
        elif self.tiebreak == 'LEFT':
            return index[0]
        else:
            return random.choice(index)
        
        
        
    def scores_for(self, b):
        """ method that takes a Board object b and determines the called 
            AIPlayer‘s scores for the columns in b
        """
        scores = b.width * [0]
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead -1)
                score = opponent.scores_for(b)
                scores[col] = 100 - max(score)
                b.remove_checker(col)
        return scores
    
    
    def next_move(self, b):
        """ method that returns the called AIPlayer‘s judgment of its best 
            possible move
        """
        self.num_moves += 1
        s = self.scores_for(b)
        max_score = self.max_score_column(s)
        return max_score       

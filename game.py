from player import HumanPlayer, GeniusComputerPlayer, RandomComputerPlayer
import time
from tqdm import tqdm
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]#we will use a single list to rep a 3x3 board
        self.current_winner = None #keep track of winner
        
    def print_board(self):
        #getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+'| '.join(row)+ '| ')
            
    @staticmethod
    def print_board_nums():
        #0 |1 |
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board:
            print('| '+'| '.join(row)+ '| ')
            
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #moves = []
        #for (i, spot) in enumerate(self.board):
            #['x','x','o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #    if spot == ' ':
        #        moves.append(i)
        #return moves
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        #if valid move, then make the move(assign square to letter)
        # then return true, if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #winner  if 3 in a row anywhere, we have check all of them
        # rows
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        #columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #diagonal
        #(0,2,4, 6, 8)
        #these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i  in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True  
            diagonal2 = [self.board[i] for i  in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #if all of these fail
        return False
        
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        
    letter = 'X'#starting letter
    #iterate while the game still has empty squares
    # we dont have to worry about winner because we'll just return that 
    #which breaks the loop
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square} ')
                game.print_board()
                print('')#just a empty line 

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                    
                    
            #after we made our move, we need to alternate letter  
            letter = 'O' if letter == 'X' else 'X'#switch player
            #if letter = 'X':
                #letter = 'O'
            #else:
            #letter = 'X'    
        time.sleep(0.5)
    if print_game:
        print("It's a tie. ")
    
if __name__== "__main__":
    '''x_wins = 0
    o_wins = 0
    tie = 0
    for _ in tqdm(range(10)):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            tie += 1 
    print(f"After 100 iterations., we see {x_wins}x wins, {o_wins} o wins and {tie} ties  ")'''
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

import random
import math
class tictactoe:
    def __init__(self):
        self.board = []
        self.human = "x"
        self.ai = "o"
        self.curr_move = None
        self.score_Map = {
              "x": -10,
              "o": 10,
              "tie": 0
            }
        for i in range(9):
            self.board.append(' ')
        print(self.board)
    
    def print_board(self):
        print(self.board[0] + ' : ' + self.board[1] + ' : ' + self.board[2] + '\n---------\n' + self.board[3] + ' : ' +self.board[4] + ' : ' + self.board[5] + '\n---------\n' + self.board[6] + ' : ' + self.board[7] + ' : ' +self.board[8])
    
    def player_move(self):
        print("the numbers you can use now are :")
        for i in range(9):
            if self.board[i] == ' ':                                    #Check Available Options
                print(i)
        move = input('please, enter a number from the list above')
        move = int(move)
        if self.board[move] == ' ':
            self.board[move] = self.human
            game.print_board()
        else:
            print('the cell is occupied ! choose other cell')
            game.player_move()

    def check_board(self):                                                       # Win/Tie check
        count = 0
        comb_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in range(8):
            if self.board[comb_win[i][0]] == self.board[comb_win[i][1]] == self.board[comb_win[i][2]] and self.board[comb_win[i][0]] != ' ':
                print('the winner is : {}'.format(self.board[comb_win[i][0]]))
                return True
        for j in range(9):
                if self.board[j] != ' ':
                    count += 1
                    if count == 9:
                        print('draw')
                        return True
        return False

    def check_board_for_minimax(self):                                                     # Win/Tie check -- > used only for the best_move function !
            count = 0
            comb_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for i in range(8):
                if self.board[comb_win[i][0]] == self.board[comb_win[i][1]] == self.board[comb_win[i][2]] and self.board[comb_win[i][0]] != ' ':
                    return self.board[comb_win[i][0]]
            for j in range(9):
                    if self.board[j] != ' ':
                        count += 1
                        if count == 9:
                            return "tie"

    def best_move(self):
        best_score=-math.inf
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i]=self.ai
                score=game.minimax(self.board, 0, False)
                self.board[i]=' '
                if score>best_score:
                    best_score=score
                    curr_move=i
        self.board[curr_move]=self.ai    
        game.print_board()
        game.check_board()

    def minimax(self,board,depth,isMaximizing):
        result = game.check_board_for_minimax()
        if (result == "x" or result =="o" or result == "tie"):
            return self.score_Map[result]

        if (isMaximizing):
            best_score=-math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i]=self.ai
                    score=self.minimax(self.board,depth+1,False)
                    self.board[i]=' '
                    best_score=max(score,best_score)
            return best_score
        else :
            best_score=math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i]=self.human
                    score=self.minimax(self.board,depth+1,True)
                    self.board[i]=' '
                    best_score=min(score,best_score)
            return best_score


game = tictactoe()
while game.check_board() == False:
    game.player_move()
    game.check_board()
    game.best_move()
   

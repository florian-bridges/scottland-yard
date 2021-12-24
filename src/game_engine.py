import numpy as np
import pickle


from board import Board


class Game_Engine:

    def to_onehot(self,dim,index):
        vector = np.zeros(dim)
        vector[index] = 1
        return vector
    
    def to_nhot(self,dim,indices):
        vector = np.zeros(dim)
        for index in indices:
            vector[index] = 1
        return vector

    def move_mr_x(self):
        simple_board = self.board.board.sum(axis=0) > 0
        N = self.board.N
        
        mrx_pos = self.to_onehot(N,self.board.player_pos[0]) 
        player_pos = self.to_nhot(N,self.board.player_pos[1:]) 


        best_path = np.zeros(N)
        for j in range(N):
            if not simple_board.dot(mrx_pos)[j]:
                continue
            player_state = player_pos
            x_state = self.to_onehot(N,j) 

            for i in range(3):
                possible = np.logical_and(np.logical_not(np.logical_or(np.logical_not(x_state),simple_board.dot(player_state) > 0)),np.logical_not(player_state))
                player_state = simple_board.dot(player_state) > 0
                x_state = simple_board.dot(x_state) > 0
                if possible.sum() == 0:
                    print("mrx can be found in ", i+1,"steps in ", int(j))
                    break
            best_path[j] = i
        best_path =np.multiply(best_path == np.max(best_path),simple_board.dot(simple_board).sum(axis=1))
        self.board.set_player_pos(0,np.argmax(best_path))

    def check_win_cond(self):
        mrx_pos = self.board.player_pos[0]
        for player_index in range(1,len(self.board.player_pos)):
            player_pos = self.board.player_pos[player_index]
            if mrx_pos == player_pos:
                print("Mr. X was found by player%s at position %s" %(player_index,player_pos + 1))
                self.mrx_found = True
                break

    def print_player_options(self, player):
        result_str = ""
        transp_modes = ["Taxi", "Bus", "Underground", "Boat"]
        for transp_mode in range(4):
            if self.board.board[transp_mode, self.board.player_pos[player],:].sum() > 0:
                result_str += transp_modes[transp_mode] + ": "
                for i in range(self.board.N):
                    if self.board.board[transp_mode, self.board.player_pos[player],i] > 0:
                        result_str +=  str(i + 1) + " "
        print(result_str)

    def move_players(self):
        while not self.mrx_found:
            for player_index in range(len(self.board.player_pos)):
                if player_index == 0:
                    self.move_mr_x()
                    continue
                self.print_player_options(player_index)
                new_pos = int(input("move player%s from %s to ?" %(player_index, self.board.player_pos[player_index] +1) )) -1
                self.board.set_player_pos(player_index, new_pos)
                self.check_win_cond()

    def __init__(self,num_players):
        self.board = Board(num_players)
        self.mrx_found = False
        pass

if __name__ == "__main__":
    ge = Game_Engine(6)
    ge.move_players()

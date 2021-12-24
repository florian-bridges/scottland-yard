import numpy as np
import pickle
from random import randrange

class Board:

    def init_player_pos(self,num_players):

        init_stops = [13,26,29,34,50,53,91,94,103,112,117,132,138,141,155,174,197,198]
        self.player_pos = [0]*num_players
        for player_index in range(len(self.player_pos)): 
            self.player_pos[player_index] = init_stops[randrange(len(init_stops))] -1 
            init_stops.remove(self.player_pos[player_index] + 1)
            print("player%s initialized at position:  %s" %(player_index, self.player_pos[player_index] + 1))

    def set_player_pos(self,player,pos):
        print("player %s changed from pos %s \t  to %s " %(player, self.player_pos[player] + 1, pos + 1) )
        self.player_pos[player] = int(pos)

    def __init__(self, num_players):
        self.board = pickle.load(open("rides.pkl","rb"))
        self.N = self.board.shape[1]
        self.init_player_pos(num_players)

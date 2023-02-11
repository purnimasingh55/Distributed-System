'''
Contains all the information about the game:
Did palyer 1 make move
Did player 2 make move
are both of them connected to server
keeping track of who won and who loose

'''

class Game:
    def __init__(self, id):
        #keeping track of which player move
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        #each game has a uniue id to keep track of what client are part of what
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0] #[player1,player2]
        self.ties = 0

    def get_player_move(self, p):
        #get the player move in range [0,1]
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True
            
    #tells weather the two players are currently connected to the game
    def connected(self):
        return self.ready
    #tells if both players have gone
    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
        #we just wanna to get first letter of move
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
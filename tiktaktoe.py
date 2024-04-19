# the file content a class TicTacToe which is a game of tiktaktoe


class TiktaktowGame(object):
    """This class is a game of tiktaktoe
    
    """
    WINNINW_COMBINATIONS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical
        (0, 4, 8), (2, 4, 6) # diagonal
    ]

    def __init__(self, player1_simbol="X", player2_simbol="O") -> None:
        self.player1_simbol = player1_simbol
        self.player2_simbol = player2_simbol
        self.board = [" " for _ in range(9)]
        self.turn = player1_simbol
        self.round = 1
        self.is_game_over = False
        # save the position played by the player and the round
        self.value_played = {}


    def check_winner(self):
        for a, b, c in self.WINNINW_COMBINATIONS:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.is_game_over = True
        return self.is_game_over
    
    def count_empty(self):
        return self.board.count(" ")

    def play(self, position):
        # run one turn depending on the the current turn and check if there is a winner
        if self.board[position] == " ":
            self.board[position] = self.turn
        # save the position played by the player and the round
        self.value_played[self.round] = position
        if self.count_empty() < 3:
            # clear the oldest value played
            pos = self.value_played.pop(self.round - 6)
            self.board[pos] = " "
        self.round += 1
        self.turn = self.player1_simbol if self.turn == self.player2_simbol else self.player2_simbol
        return self.check_winner()
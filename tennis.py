class Tennis(object):

    def __init__(self):

        self.first_player_score_times = 0
        self.second_player_score_times = 0
        self.score_lookup = {
            0:'love', 
            1:'fifteen', 
            2:'thirty',
            3:'fourty'
        }

    def score(self):

        if self.first_player_score_times == self.second_player_score_times:
            if self.first_player_score_times == 0:
                return "love_all"
            elif self.first_player_score_times == 1:
                return "fifteen_all"
            elif self.first_player_score_times == 2:
                return "thirty_all"
            else:
                return "deuce"

        if self.first_player_score_times > self.second_player_score_times and self.first_player_score_times <= 3:
            return self.score_lookup[self.first_player_score_times]+'_'+self.score_lookup[self.second_player_score_times]        

        if self.first_player_score_times > 3 or self.second_player_score_times > 3:
            diff = self.first_player_score_times - self.second_player_score_times
            if diff == 1:
                return "first_player_advantage" 
            if diff == -1:
                return "second_player_advantage"
            if diff > 1:
                return "first_player_win"
            if diff < -1:
                return "second_player_win"

    def first_player_score(self):
        self.first_player_score_times += 1

    def second_player_score(self):
        self.second_player_score_times += 1
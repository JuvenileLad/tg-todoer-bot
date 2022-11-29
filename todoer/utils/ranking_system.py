class RankingSystem:
    def __init__(self):
        self.rank_list = {0:'Unranked',1:'Aleph', 2:'Bet', 3:'Gimmel', 4:'Daleth'}
    
    def RankUp(self, CurrentRank_int):
        return self.rank_list[CurrentRank_int+1]
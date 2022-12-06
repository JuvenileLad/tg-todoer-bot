class RankingSystem:
    def __init__(self, Mana):
        self.rank_list = {1:'Unranked',90:'ALEPH', 178:'BET', 266:'GIMMEL', 354:'DALETH'}
        self.rank_symbol = {'Unranked':'', 'ALEPH':'א', 'BET':'ב', 'GIMMEL':'ג', 'DALETH':'ד'}
        self.Mana = Mana
    
    def getRank(self):
        num = 0
        for RequiredMana in self.rank_list:
            num+=1
            if self.Mana == RequiredMana:
                playerRank = self.rank_list[RequiredMana]
                break
            if self.Mana > RequiredMana and self.Mana < (2+(num*((88)))-RequiredMana)+RequiredMana:
                playerRank = self.rank_list[RequiredMana]
                break
        return [playerRank, self.rank_symbol[playerRank]]
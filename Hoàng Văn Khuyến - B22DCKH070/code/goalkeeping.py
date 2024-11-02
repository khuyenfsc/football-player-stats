class Goalkeeping:
    __performance = "N/A"
    __penalty_kicks = "N/A"

    def __init__(self, performance="N/A", penalty_kicks="N/A"):
        self.__performance = performance
        self.__penalty_kicks = penalty_kicks
        
    def get_performance(self):
        return self.__performance

    def get_penalty_kicks(self):
        return self.__penalty_kicks
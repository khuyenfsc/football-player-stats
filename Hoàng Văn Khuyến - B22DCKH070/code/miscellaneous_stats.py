class MiscellaneousStats:
    __performance = "N/A"
    __aerial_duels = "N/A"

    def __init__(self, performance="N/A", aerial_duels="N/A"):
        self.__performance = performance
        self.__aerial_duels = aerial_duels

    def get_performance(self):
        return self.__performance

    def get_aerial_duels(self):
        return self.__aerial_duels
class AerialDuels:
    __won = "N/A"
    __lost = "N/A"
    __won_percentage = "N/A"

    def __init__(self, won="N/A", lost="N/A", won_percentage="N/A"):
        self.__won = won
        self.__lost = lost
        self.__won_percentage = won_percentage

    def get_won(self):
        return self.__won

    def get_lost(self):
        return self.__lost

    def get_won_percentage(self):
        return self.__won_percentage
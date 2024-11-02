class Possession:
    __touches = "N/A"
    __take_ons = "N/A"
    __carries = "N/A"
    __receiving = "N/A"

    def __init__(self, touches="N/A", take_ons="N/A", carries="N/A", receiving="N/A"):
        self.__touches = touches
        self.__take_ons = take_ons
        self.__carries = carries
        self.__receiving = receiving


    def get_touches(self):
        return self.__touches

    def get_take_ons(self):
        return self.__take_ons

    def get_carries(self):
        return self.__carries

    def get_receiving(self):
        return self.__receiving
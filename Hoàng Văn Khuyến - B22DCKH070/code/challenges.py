class Challenges:
    __tkl = "N/A"
    __att = "N/A"
    __tkl_percentage = "N/A"
    __lost = "N/A"

    def __init__(self, tkl="N/A", att="N/A", tkl_percentage="N/A", lost="N/A"):
        self.__tkl = tkl
        self.__att = att
        self.__tkl_percentage = tkl_percentage
        self.__lost = lost

    def get_tkl(self):
        return self.__tkl

    def get_att(self):
        return self.__att

    def get_tkl_percentage(self):
        return self.__tkl_percentage

    def get_lost(self):
        return self.__lost
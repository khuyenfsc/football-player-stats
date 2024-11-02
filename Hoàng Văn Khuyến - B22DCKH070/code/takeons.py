class TakeOns:
    __att = "N/A"
    __succ = "N/A"
    __succ_percentage = "N/A"
    __tkld = "N/A"
    __tkld_percentage = "N/A"

    def __init__(self, att="N/A", succ="N/A", succ_percentage="N/A", tkld="N/A", tkld_percentage="N/A"):
        self.__att = att
        self.__succ = succ
        self.__succ_percentage = succ_percentage
        self.__tkld = tkld
        self.__tkld_percentage = tkld_percentage


    def get_att(self):
        return self.__att

    def get_succ(self):
        return self.__succ

    def get_succ_percentage(self):
        return self.__succ_percentage

    def get_tkld(self):
        return self.__tkld

    def get_tkld_percentage(self):
        return self.__tkld_percentage
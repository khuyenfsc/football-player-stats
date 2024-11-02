class Tackles:
    __tkl = "N/A"
    __tklw = "N/A"
    __def_3rd = "N/A"
    __mid_3rd = "N/A"
    __att_3rd = "N/A"

    def __init__(self, tkl="N/A", tklw="N/A", def_3rd="N/A", mid_3rd="N/A", att_3rd="N/A"):
        self.__tkl = tkl
        self.__tklw = tklw
        self.__def_3rd = def_3rd
        self.__mid_3rd = mid_3rd
        self.__att_3rd = att_3rd


    def get_tkl(self):
        return self.__tkl

    def get_tklw(self):
        return self.__tklw

    def get_def_3rd(self):
        return self.__def_3rd

    def get_mid_3rd(self):
        return self.__mid_3rd

    def get_att_3rd(self):
        return self.__att_3rd
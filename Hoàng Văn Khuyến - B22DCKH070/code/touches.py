class Touches:
    __touches = "N/A"
    __def_pen = "N/A"
    __def_3rd = "N/A"
    __mid_3rd = "N/A"
    __att_3rd = "N/A"
    __att_pen = "N/A"
    __live = "N/A"

    def __init__(self, touches="N/A", def_pen="N/A", def_3rd="N/A", mid_3rd="N/A", att_3rd="N/A", att_pen="N/A", live="N/A"):
        self.__touches = touches
        self.__def_pen = def_pen
        self.__def_3rd = def_3rd
        self.__mid_3rd = mid_3rd
        self.__att_3rd = att_3rd
        self.__att_pen = att_pen
        self.__live = live


    def get_touches(self):
        return self.__touches

    def get_def_pen(self):
        return self.__def_pen

    def get_def_3rd(self):
        return self.__def_3rd

    def get_mid_3rd(self):
        return self.__mid_3rd

    def get_att_3rd(self):
        return self.__att_3rd

    def get_att_pen(self):
        return self.__att_pen

    def get_live(self):
        return self.__live
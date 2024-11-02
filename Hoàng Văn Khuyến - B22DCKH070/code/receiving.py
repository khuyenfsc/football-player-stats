class Receiving:
    __rec = "N/A"
    __prg_r = "N/A"

    def __init__(self, rec="N/A", prg_r="N/A"):
        self.__rec = rec
        self.__prg_r = prg_r


    def get_rec(self):
        return self.__rec

    def get_prg_r(self):
        return self.__prg_r
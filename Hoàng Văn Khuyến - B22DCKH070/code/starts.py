class Starts:
    __starts = "N/A"
    __mn_per_start = "N/A"
    __compl = "N/A"

    def __init__(self, starts="N/A", mn_per_start="N/A", compl="N/A"):
        self.__starts = starts
        self.__mn_per_start = mn_per_start
        self.__compl = compl


    def get_starts(self):
        return self.__starts

    def get_mn_per_start(self):
        return self.__mn_per_start

    def get_compl(self):
        return self.__compl
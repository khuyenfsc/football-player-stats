class Progression:
    __PrgC = "N/A"
    __PrgP = "N/A"
    __PrgR = "N/A"

    def __init__(self, prg_c="N/A", prg_p="N/A", prg_r="N/A"):
        self.__PrgC = prg_c
        self.__PrgP = prg_p
        self.__PrgR = prg_r


    def get_prg_c(self):
        return self.__PrgC

    def get_prg_p(self):
        return self.__PrgP

    def get_prg_r(self):
        return self.__PrgR

    def print_info(self):
        print(f"Progression C: {self.__PrgC}")
        print(f"Progression P: {self.__PrgP}")
        print(f"Progression R: {self.__PrgR}")
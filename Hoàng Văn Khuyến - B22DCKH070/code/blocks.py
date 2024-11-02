class Blocks:
    __blocks = "N/A"
    __sh = "N/A"
    __pass = "N/A"
    __int = "N/A"
    __tkl_plus_int = "N/A"
    __clr = "N/A"
    __err = "N/A"

    def __init__(self, blocks="N/A", sh="N/A", pass_="N/A", int_="N/A", tkl_plus_int="N/A", clr="N/A", err="N/A"):
        self.__blocks = blocks
        self.__sh = sh
        self.__pass = pass_
        self.__int = int_
        self.__tkl_plus_int = tkl_plus_int
        self.__clr = clr
        self.__err = err

    def get_blocks(self):
        return self.__blocks

    def get_sh(self):
        return self.__sh

    def get_pass(self):
        return self.__pass

    def get_int(self):
        return self.__int

    def get_tkl_plus_int(self):
        return self.__tkl_plus_int

    def get_clr(self):
        return self.__clr

    def get_err(self):
        return self.__err
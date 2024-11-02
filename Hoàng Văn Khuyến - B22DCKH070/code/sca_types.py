class SCATypes:
    __pass_live = "N/A"
    __pass_dead = "N/A"
    __to = "N/A"
    __sh = "N/A"
    __fld = "N/A"
    __def = "N/A"

    def __init__(self, pass_live="N/A", pass_dead="N/A", to="N/A", sh="N/A", fld="N/A", def_="N/A"):
        self.__pass_live = pass_live
        self.__pass_dead = pass_dead
        self.__to = to
        self.__sh = sh
        self.__fld = fld
        self.__def = def_


    def get_pass_live(self):
        return self.__pass_live

    def get_pass_dead(self):
        return self.__pass_dead

    def get_to(self):
        return self.__to

    def get_sh(self):
        return self.__sh

    def get_fld(self):
        return self.__fld

    def get_def(self):
        return self.__def
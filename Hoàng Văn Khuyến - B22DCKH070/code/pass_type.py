class PassType:
    __live = "N/A"
    __dead = "N/A"
    __fk = "N/A"
    __tb = "N/A"
    __sw = "N/A"
    __crs = "N/A"
    __ti = "N/A"
    __ck = "N/A"

    def __init__(self, live="N/A", dead="N/A", fk="N/A", tb="N/A", sw="N/A", crs="N/A", ti="N/A", ck="N/A"):
        self.__live = live
        self.__dead = dead
        self.__fk = fk
        self.__tb = tb
        self.__sw = sw
        self.__crs = crs
        self.__ti = ti
        self.__ck = ck

    def get_live(self):
        return self.__live

    def get_dead(self):
        return self.__dead

    def get_fk(self):
        return self.__fk

    def get_tb(self):
        return self.__tb

    def get_sw(self):
        return self.__sw

    def get_crs(self):
        return self.__crs

    def get_ti(self):
        return self.__ti

    def get_ck(self):
        return self.__ck

    def print_info(self):
        print(f"Live Passes: {self.__live}")
        print(f"Dead Ball Passes: {self.__dead}")
        print(f"Free Kick Passes: {self.__fk}")
        print(f"Throw-In Passes: {self.__tb}")
        print(f"Short Passes: {self.__sw}")
        print(f"Crosses: {self.__crs}")
        print(f"Throw Ins: {self.__ti}")
        print(f"Corner Kicks: {self.__ck}")
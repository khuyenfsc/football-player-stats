class MiscellaneousPerformance:
    __fls = "N/A"
    __fld = "N/A"
    __off = "N/A"
    __crs = "N/A"
    __og = "N/A"
    __recov = "N/A"

    def __init__(self, fls="N/A", fld="N/A", off="N/A", crs="N/A", og="N/A", recov="N/A"):
        self.__fls = fls
        self.__fld = fld
        self.__off = off
        self.__crs = crs
        self.__og = og
        self.__recov = recov

    def get_fls(self):
        return self.__fls

    def get_fld(self):
        return self.__fld

    def get_off(self):
        return self.__off

    def get_crs(self):
        return self.__crs

    def get_og(self):
        return self.__og

    def get_recov(self):
        return self.__recov
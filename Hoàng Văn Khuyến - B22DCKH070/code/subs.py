class Subs:
    __subs = "N/A"
    __mn_per_sub = "N/A"
    __un_sub = "N/A"

    def __init__(self, subs="N/A", mn_per_sub="N/A", un_sub="N/A"):
        self.__subs = subs
        self.__mn_per_sub = mn_per_sub
        self.__un_sub = un_sub


    def get_subs(self):
        return self.__subs

    def get_mn_per_sub(self):
        return self.__mn_per_sub

    def get_un_sub(self):
        return self.__un_sub
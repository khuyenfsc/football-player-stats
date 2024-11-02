class TeamSuccess:
    __ppm = "N/A"
    __on_g = "N/A"
    __on_ga = "N/A"

    def __init__(self, ppm="N/A", on_g="N/A", on_ga="N/A"):
        self.__ppm = ppm
        self.__on_g = on_g
        self.__on_ga = on_ga


    def get_ppm(self):
        return self.__ppm

    def get_on_g(self):
        return self.__on_g

    def get_on_ga(self):
        return self.__on_ga

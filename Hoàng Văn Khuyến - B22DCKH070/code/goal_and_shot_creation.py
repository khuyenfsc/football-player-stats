class GoalAndShotCreation:
    __sca = "N/A"
    __sca_types = "N/A"
    __gca = "N/A"
    __gca_types = "N/A"

    def __init__(self, sca="N/A", sca_types="N/A", gca="N/A", gca_types="N/A"):
        self.__sca = sca
        self.__sca_types = sca_types
        self.__gca = gca
        self.__gca_types = gca_types

    def get_sca(self):
        return self.__sca

    def get_sca_types(self):
        return self.__sca_types

    def get_gca(self):
        return self.__gca

    def get_gca_types(self):
        return self.__gca_types
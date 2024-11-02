class SCA:
    __sca = "N/A"
    __sca90 = "N/A"

    def __init__(self, sca="N/A", sca90="N/A"):
        self.__sca = sca
        self.__sca90 = sca90


    def get_sca(self):
        return self.__sca

    def get_sca90(self):
        return self.__sca90
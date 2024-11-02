class GCA:
    __gca = "N/A"
    __gca90 = "N/A"

    def __init__(self, gca="N/A", gca90="N/A"):
        self.__gca = gca
        self.__gca90 = gca90

    def get_gca(self):
        return self.__gca

    def get_gca90(self):
        return self.__gca90
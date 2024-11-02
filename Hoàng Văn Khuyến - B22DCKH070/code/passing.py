class Passing:
    __total = "N/A"
    __short = "N/A"
    __medium = "N/A"
    __long = "N/A"
    __passing_expected = "N/A"

    def __init__(self, total="N/A", short="N/A", medium="N/A", long="N/A", passing_expected="N/A"):
        self.__total = total
        self.__short = short
        self.__medium = medium
        self.__long = long
        self.__passing_expected = passing_expected

    def get_total(self):
        return self.__total

    def get_short(self):
        return self.__short

    def get_medium(self):
        return self.__medium

    def get_long(self):
        return self.__long

    def get_passing_expected(self):
        return self.__passing_expected
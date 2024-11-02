class Shooting:
    __standard = "N/A"
    __shooting_expected = "N/A"

    def __init__(self, standard="N/A", shooting_expected="N/A"):
        self.__standard = standard
        self.__shooting_expected = shooting_expected


    def get_standard(self):
        return self.__standard

    def get_shooting_expected(self):
        return self.__shooting_expected
    
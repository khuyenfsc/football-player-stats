class PassTypes:
    __pass_type = "N/A"
    __corner_kicks = "N/A"
    __outcomes = "N/A"

    def __init__(self, pass_type="N/A", corner_kicks="N/A", outcomes="N/A"):
        self.__pass_type = pass_type
        self.__corner_kicks = corner_kicks
        self.__outcomes = outcomes

    def get_pass_type(self):
        return self.__pass_type

    def get_corner_kicks(self):
        return self.__corner_kicks

    def get_outcomes(self):
        return self.__outcomes
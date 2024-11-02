class Short:
    __Cmp = "N/A"
    __Att = "N/A"
    __Cmppercent = "N/A"

    def __init__(self, cmp="N/A", att="N/A", cmp_percent="N/A"):
        self.__Cmp = cmp
        self.__Att = att
        self.__Cmppercent = cmp_percent

    def get_cmp(self):
        return self.__Cmp

    def get_att(self):
        return self.__Att

    def get_cmp_percent(self):
        return self.__Cmppercent

    def print_info(self):
        print(f"Completed Short Passes (Cmp): {self.__Cmp}")
        print(f"Short Pass Attempts (Att): {self.__Att}")
        print(f"Short Pass Completion Percentage (Cmp%): {self.__Cmppercent}")
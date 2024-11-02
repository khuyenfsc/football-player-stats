class Medium:
    __Cmp = "N/A"
    __Att = "N/A"
    __Cmppercent = "N/A"

    def __init__(self, cmp="N/A", att="N/A", cmppercent="N/A"):
        self.__Cmp = cmp
        self.__Att = att
        self.__Cmppercent = cmppercent

    def get_cmp(self):
        return self.__Cmp

    def get_att(self):
        return self.__Att

    def get_cmppercent(self):
        return self.__Cmppercent

    def print_info(self):
        print(f"Completed Medium Passes (Cmp): {self.__Cmp}")
        print(f"Medium Pass Attempts (Att): {self.__Att}")
        print(f"Medium Pass Completion Percentage (Cmp%): {self.__Cmppercent}")
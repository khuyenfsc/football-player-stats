class Total:
    __Cmp = "N/A"
    __Att = "N/A"
    __Cmppercent = "N/A"
    __TotDist = "N/A"
    __PrgDist = "N/A"

    def __init__(self, cmp="N/A", att="N/A", cmp_percent="N/A", tot_dist="N/A", prg_dist="N/A"):
        self.__Cmp = cmp
        self.__Att = att
        self.__Cmppercent = cmp_percent
        self.__TotDist = tot_dist
        self.__PrgDist = prg_dist


    def get_cmp(self):
        return self.__Cmp

    def get_att(self):
        return self.__Att

    def get_cmp_percent(self):
        return self.__Cmppercent

    def get_tot_dist(self):
        return self.__TotDist

    def get_prg_dist(self):
        return self.__PrgDist

    def print_info(self):
        print(f"Completed Passes (Cmp): {self.__Cmp}")
        print(f"Pass Attempts (Att): {self.__Att}")
        print(f"Completion Percentage (Cmp%): {self.__Cmppercent}")
        print(f"Total Passing Distance (TotDist): {self.__TotDist} meters")
        print(f"Progressive Passing Distance (PrgDist): {self.__PrgDist} meters")

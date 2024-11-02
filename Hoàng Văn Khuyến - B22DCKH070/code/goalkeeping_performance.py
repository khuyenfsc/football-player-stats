class GoalkeepingPerformance:
    __GA = "N/A"
    __GA90 = "N/A"
    __SoTA = "N/A"
    __Saves = "N/A"
    __Savepercent = "N/A"
    __W = "N/A"
    __D = "N/A"
    __L = "N/A"
    __CS = "N/A"
    __CSpercent = "N/A"

    def __init__(self, ga="N/A", ga90="N/A", sota="N/A", saves="N/A", save_percent="N/A", w="N/A", d="N/A", l="N/A", cs="N/A", cs_percent="N/A"):
        self.__GA = ga
        self.__GA90 = ga90
        self.__SoTA = sota
        self.__Saves = saves
        self.__Savepercent = save_percent
        self.__W = w
        self.__D = d
        self.__L = l
        self.__CS = cs
        self.__CSpercent = cs_percent
        
    def get_ga(self):
        return self.__GA

    def get_ga90(self):
        return self.__GA90

    def get_sota(self):
        return self.__SoTA

    def get_saves(self):
        return self.__Saves

    def get_save_percent(self):
        return self.__Savepercent

    def get_w(self):
        return self.__W

    def get_d(self):
        return self.__D

    def get_l(self):
        return self.__L

    def get_cs(self):
        return self.__CS

    def get_cs_percent(self):
        return self.__CSpercent

    def print_info(self):
        print(f"Goals Against (GA): {self.__GA}")
        print(f"Goals Against per 90 minutes (GA90): {self.__GA90}")
        print(f"Saves on Target Against (SoTA): {self.__SoTA}")
        print(f"Saves: {self.__Saves}")
        print(f"Save Percentage: {self.__Savepercent}")
        print(f"Wins (W): {self.__W}")
        print(f"Draws (D): {self.__D}")
        print(f"Losses (L): {self.__L}")
        print(f"Clean Sheets (CS): {self.__CS}")
        print(f"Clean Sheet Percentage: {self.__CSpercent}")

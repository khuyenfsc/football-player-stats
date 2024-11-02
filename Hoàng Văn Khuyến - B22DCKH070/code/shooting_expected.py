class ShootingExpected:
    __xG = "N/A"
    __npxG = "N/A"
    __npxG_per_Sh = "N/A"
    __G_minus_xG = "N/A"
    __np_G_minus_xG = "N/A"

    def __init__(self, xG="N/A", npxG="N/A", npxG_per_sh="N/A", g_minus_xG="N/A", np_g_minus_xG="N/A"):
        self.__xG = xG
        self.__npxG = npxG
        self.__npxG_per_Sh = npxG_per_sh
        self.__G_minus_xG = g_minus_xG
        self.__np_G_minus_xG = np_g_minus_xG


    def get_xG(self):
        return self.__xG

    def get_npxG(self):
        return self.__npxG

    def get_npxG_per_sh(self):
        return self.__npxG_per_Sh

    def get_g_minus_xG(self):
        return self.__G_minus_xG

    def get_np_g_minus_xG(self):
        return self.__np_G_minus_xG

    def print_info(self):
        print(f"Expected Goals (xG): {self.__xG}")
        print(f"Non-penalty Expected Goals (npxG): {self.__npxG}")
        print(f"Non-penalty xG per Shot: {self.__npxG_per_Sh}")
        print(f"Goals minus Expected Goals (G - xG): {self.__G_minus_xG}")
        print(f"Non-penalty Goals minus Expected Goals (npG - xG): {self.__np_G_minus_xG}")

class Per90Minutes:
    __Gls = "N/A"
    __Ast = "N/A"
    __G_plus_A = "N/A"
    __G_minus_PK = "N/A"
    __G_plus_A_minus_PK = "N/A"
    __xG = "N/A"
    __xAG = "N/A"
    __xG_plus_xAG = "N/A"
    __npxG = "N/A"
    __npxG_plus_xAG = "N/A"

    def __init__(self, gls="N/A", ast="N/A", g_plus_a="N/A", g_minus_pk="N/A", g_plus_a_minus_pk="N/A", xG="N/A", xAG="N/A", xG_plus_xAG="N/A", npxG="N/A", npxG_plus_xAG="N/A"):
        self.__Gls = gls
        self.__Ast = ast
        self.__G_plus_A = g_plus_a
        self.__G_minus_PK = g_minus_pk
        self.__G_plus_A_minus_PK = g_plus_a_minus_pk
        self.__xG = xG
        self.__xAG = xAG
        self.__xG_plus_xAG = xG_plus_xAG
        self.__npxG = npxG
        self.__npxG_plus_xAG = npxG_plus_xAG

    def get_gls(self):
        return self.__Gls

    def get_ast(self):
        return self.__Ast

    def get_g_plus_a(self):
        return self.__G_plus_A

    def get_g_minus_pk(self):
        return self.__G_minus_PK

    def get_g_plus_a_minus_pk(self):
        return self.__G_plus_A_minus_PK

    def get_xG(self):
        return self.__xG

    def get_xAG(self):
        return self.__xAG

    def get_xG_plus_xAG(self):
        return self.__xG_plus_xAG

    def get_npxG(self):
        return self.__npxG

    def get_npxG_plus_xAG(self):
        return self.__npxG_plus_xAG

    def print_info(self):
        print(f"Goals: {self.__Gls}")
        print(f"Assists: {self.__Ast}")
        print(f"Goals + Assists: {self.__G_plus_A}")
        print(f"Goals - Penalty Kicks: {self.__G_minus_PK}")
        print(f"Goals + Assists - Penalty Kicks: {self.__G_plus_A_minus_PK}")
        print(f"xG: {self.__xG}")
        print(f"xAG: {self.__xAG}")
        print(f"xG + xAG: {self.__xG_plus_xAG}")
        print(f"npxG: {self.__npxG}")
        print(f"npxG + xAG: {self.__npxG_plus_xAG}")
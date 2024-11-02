class PassingExpected:
    __Ast = "N/A"
    __xAG = "N/A"
    __xA = "N/A"
    __A_minus_xAG = "N/A"
    __KP = "N/A"
    __one_third = "N/A"
    __PPA = "N/A"
    __CrsPA = "N/A"
    __PrgP = "N/A"

    def __init__(self, ast="N/A", xAG="N/A", xA="N/A", a_minus_xAG="N/A", kp="N/A", one_third="N/A", ppa="N/A", crsPA="N/A", prgP="N/A"):
        self.__Ast = ast
        self.__xAG = xAG
        self.__xA = xA
        self.__A_minus_xAG = a_minus_xAG
        self.__KP = kp
        self.__one_third = one_third
        self.__PPA = ppa
        self.__CrsPA = crsPA
        self.__PrgP = prgP

    def get_ast(self):
        return self.__Ast

    def get_xAG(self):
        return self.__xAG

    def get_xA(self):
        return self.__xA

    def get_a_minus_xAG(self):
        return self.__A_minus_xAG

    def get_kp(self):
        return self.__KP

    def get_one_third(self):
        return self.__one_third

    def get_ppa(self):
        return self.__PPA

    def get_crsPA(self):
        return self.__CrsPA

    def get_prgP(self):
        return self.__PrgP

    def print_info(self):
        print(f"Assists (Ast): {self.__Ast}")
        print(f"Expected Assists (xAG): {self.__xAG}")
        print(f"Expected Assists (xA): {self.__xA}")
        print(f"Assists minus Expected Assists (A - xAG): {self.__A_minus_xAG}")
        print(f"Key Passes (KP): {self.__KP}")
        print(f"One Third Passes: {self.__one_third}")
        print(f"Passes Per Attempt (PPA): {self.__PPA}")
        print(f"Crosses Per Attempt (CrsPA): {self.__CrsPA}")
        print(f"Progressive Passes (PrgP): {self.__PrgP}")
class StandardExpected:
    __xG = "N/A"
    __npxG = "N/A"
    __xAG = "N/A"

    def __init__(self, xG="N/A", npxG="N/A", xAG="N/A"):
        self.__xG = xG
        self.__npxG = npxG
        self.__xAG = xAG


    def get_xG(self):
        return self.__xG

    def get_npxG(self):
        return self.__npxG

    def get_xAG(self):
        return self.__xAG
    
    def print_info(self):
        print(f"xG: {self.__xG}")
        print(f"npxG: {self.__npxG}")
        print(f"xAG: {self.__xAG}")
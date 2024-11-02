class CornerKicks:
    __in_kick = "N/A"
    __out_kick = "N/A"
    __str_kick = "N/A"

    def __init__(self, in_kick="N/A", out_kick="N/A", str_kick="N/A"):
        self.__in_kick = in_kick
        self.__out_kick = out_kick
        self.__str_kick = str_kick
        
    def get_in_kick(self):
        return self.__in_kick

    def get_out_kick(self):
        return self.__out_kick

    def get_str_kick(self):
        return self.__str_kick

    def print_info(self):
        print(f"In Corner Kicks: {self.__in_kick}")
        print(f"Out Corner Kicks: {self.__out_kick}")
        print(f"Straight Corner Kicks: {self.__str_kick}")
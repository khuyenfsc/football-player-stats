class Outcomes:
    __cmp = "N/A"
    __off = "N/A"
    __blocks = "N/A"

    def __init__(self, cmp="N/A", off="N/A", blocks="N/A"):
        self.__cmp = cmp
        self.__off = off
        self.__blocks = blocks

    def get_cmp(self):
        return self.__cmp

    def get_off(self):
        return self.__off

    def get_blocks(self):
        return self.__blocks

    def print_info(self):
        print(f"Completed Outcomes (Cmp): {self.__cmp}")
        print(f"Off-target Outcomes: {self.__off}")
        print(f"Blocked Outcomes: {self.__blocks}")
class DefensiveActions:
    __tackles = "N/A"
    __challenges = "N/A"
    __blocks = "N/A"

    def __init__(self, tackles="N/A", challenges="N/A", blocks="N/A"):
        self.__tackles = tackles
        self.__challenges = challenges
        self.__blocks = blocks

    def get_tackles(self):
        return self.__tackles

    def get_challenges(self):
        return self.__challenges

    def get_blocks(self):
        return self.__blocks
class Performance:
    __non_penalty_goals = "N/A"
    __penalty_goals = "N/A"
    __assists = "N/A"
    __yellow_cards = "N/A"
    __red_cards = "N/A"

    def __init__(self, non_penalty_goals="N/A", penalty_goals="N/A", assists="N/A", yellow_cards="N/A", red_cards="N/A"):
        self.__non_penalty_goals = non_penalty_goals
        self.__penalty_goals = penalty_goals
        self.__assists = assists
        self.__yellow_cards = yellow_cards
        self.__red_cards = red_cards
        
    def get_non_penalty_goals(self):
        return self.__non_penalty_goals

    def get_penalty_goals(self):
        return self.__penalty_goals

    def get_assists(self):
        return self.__assists

    def get_yellow_cards(self):
        return self.__yellow_cards

    def get_red_cards(self):
        return self.__red_cards

    def print_info(self):
        print(f"Non-Penalty Goals: {self.__non_penalty_goals}")
        print(f"Penalty Goals: {self.__penalty_goals}")
        print(f"Assists: {self.__assists}")
        print(f"Yellow Cards: {self.__yellow_cards}")
        print(f"Red Cards: {self.__red_cards}")
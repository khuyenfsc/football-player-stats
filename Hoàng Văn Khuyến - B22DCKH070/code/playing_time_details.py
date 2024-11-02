class PlayingTimeDetails:
    __starts = "N/A"
    __subs = "N/A"
    __team_success = "N/A"
    __team_success_xg = "N/A"

    def __init__(self, starts="N/A", subs="N/A", team_success="N/A", team_success_xg="N/A"):
        self.__starts = starts
        self.__subs = subs
        self.__team_success = team_success
        self.__team_success_xg = team_success_xg

    def get_starts(self):
        return self.__starts

    def get_subs(self):
        return self.__subs

    def get_team_success(self):
        return self.__team_success

    def get_team_success_xg(self):
        return self.__team_success_xg
class PlayingTime:
    __matches_played = "N/A"
    __starts = "N/A"
    __minutes = "N/A"
    __played_minutes = "N/A"

    def __init__(self, matches_played="N/A", starts="N/A", minutes="N/A", played_minutes="N/A"):
        self.__matches_played = matches_played
        self.__starts = starts
        self.__minutes = minutes
        self.__played_minutes = played_minutes

    def get_matches_played(self):
        return self.__matches_played

    def get_starts(self):
        return self.__starts

    def get_minutes(self):
        return self.__minutes

    def get_played_minutes(self):
        return self.__played_minutes

    def print_info(self):
        print(f"Matches Played: {self.__matches_played}")
        print(f"Starts: {self.__starts}")
        print(f"Minutes: {self.__minutes}")
        print(f"Played Minutes: {self.__played_minutes}")
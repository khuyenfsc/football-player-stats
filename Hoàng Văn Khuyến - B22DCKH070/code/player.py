from goalkeeping_performance import GoalkeepingPerformance
from penalty_kicks import PenaltyKicks
from goalkeeping import Goalkeeping
from shooting_standard import ShootingStandard
from shooting_expected import ShootingExpected
from shooting import Shooting
from passing import Passing
from total import Total
from short import Short
from medium import Medium
from long import Long
from passing_expected import PassingExpected
from pass_types import PassTypes
from pass_type import PassType
from corner_kicks import CornerKicks
from outcomes import Outcomes
from goal_and_shot_creation import GoalAndShotCreation
from sca import SCA
from gca import GCA
from sca_types import SCATypes
from gca_types import GCATypes
from defensive_actions import DefensiveActions
from tackles import Tackles
from challenges import Challenges
from blocks import Blocks
from possession import Possession
from touches import Touches
from takeons import TakeOns
from carries import Carries
from receiving import Receiving
from playing_time_details import PlayingTimeDetails
from starts import Starts
from subs import Subs
from team_success import TeamSuccess
from team_success_xg import TeamSuccessxG
from miscellaneous_stats import MiscellaneousStats
from miscellaneous_performance import MiscellaneousPerformance
from aerial_duels import AerialDuels

class Player:
    __name = "N/A"
    __nation = "N/A"
    __team = "N/A"
    __position = "N/A"
    __age = "N/A"
    __playing_time = "N/A"
    __performance = "N/A"
    __expected = "N/A"
    __progression = "N/A"
    __per_90_minutes = "N/A"
    __goalkeeping = Goalkeeping(GoalkeepingPerformance(), PenaltyKicks())
    __shooting = Shooting(ShootingStandard(), ShootingExpected())
    __passing = Passing(Total(), Short(), Medium(), Long(), PassingExpected())
    __pass_types = PassTypes(PassType(), CornerKicks(), Outcomes())
    __goal_and_shot_creation = GoalAndShotCreation(SCA(), SCATypes())
    __defensive_actions = DefensiveActions(Tackles(), Challenges(), Blocks())
    __possession = Possession(Touches(), TakeOns(), Carries(), Receiving())
    __playing_time_details = PlayingTimeDetails(Starts(), Subs(), TeamSuccess(), TeamSuccessxG())
    __miscellaneous_stats = MiscellaneousStats(MiscellaneousPerformance(), AerialDuels())

    def __init__(self, name="N/A", nation="N/A", team="N/A", position="N/A", age="N/A", playing_time="N/A", performance="N/A", expected="N/A", progression="N/A", per_90_minutes="N/A"):
        self.__name = name
        self.__nation = nation
        self.__team = team
        self.__position = position
        self.__age = age
        self.__playing_time = playing_time
        self.__performance = performance
        self.__expected = expected
        self.__progression = progression
        self.__per_90_minutes = per_90_minutes

    def get_name(self):
        return self.__name

    def get_nation(self):
        return self.__nation

    def get_team(self):
        return self.__team

    def get_position(self):
        return self.__position

    def get_age(self):
        return self.__age

    def get_age_for_comparing(self):
        try:
            return int(self.__age)  
        except ValueError:
            return -1

    def get_playing_time(self):
        return self.__playing_time

    def get_performance(self):
        return self.__performance

    def get_expected(self):
        return self.__expected

    def get_progression(self):
        return self.__progression

    def get_per_90_minutes(self):
        return self.__per_90_minutes

    def get_goalkeeping(self):
        return self.__goalkeeping

    def get_shooting(self):
        return self.__shooting

    def get_passing(self):
        return self.__passing

    def get_pass_types(self):
        return self.__pass_types

    def get_goal_and_shot_creation(self):
        return self.__goal_and_shot_creation

    def get_defensive_actions(self):
        return self.__defensive_actions

    def get_possession(self):
        return self.__possession

    def get_playing_time_details(self):
        return self.__playing_time_details

    def get_miscellaneous_stats(self):
        return self.__miscellaneous_stats

    def set_goalkeeping(self, value):
        self.__goalkeeping = value

    def set_shooting(self, value):
        self.__shooting = value

    def set_passing(self, value):
        self.__passing = value

    def set_pass_types(self, value):
        self.__pass_types = value

    def set_goal_and_shot_creation(self, value):
        self.__goal_and_shot_creation = value

    def set_defensive_actions(self, value):
        self.__defensive_actions = value

    def set_possession(self, value):
        self.__possession = value

    def set_playing_time_details(self, value):
        self.__playing_time_details = value

    def set_miscellaneous_stats(self, value):
        self.__miscellaneous_stats = value

    def __eq__(self, other):
        return (self.__name == other.get_name() and
                self.__nation == other.get_nation() and
                self.__position == other.get_position() and
                self.__age == other.get_age())

    def print_info(self):
        print(f"Name: {self.__name}")
        print(f"Nation: {self.__nation}")
        print(f"Team: {self.__team}")
        print(f"Position: {self.__position}")
        print(f"Age: {self.__age}")
        self.__playing_time.print_info()
        self.__performance.print_info()
        self.__expected.print_info()
        self.__progression.print_info()
        self.__per_90_minutes.print_info()
        if(self.__goalkeeping != "N/A"):
            self.__goalkeeping.get_performance().print_info()
            self.__goalkeeping.get_penalty_kicks().print_info()
        else: 
            print(None)
        
        if(self.__shooting != "N/A"):
            self.__shooting.get_standard().print_info()
            self.__shooting.get_shooting_expected().print_info()
        else: 
            print(None)
        
        if(self.__shooting != "N/A"):
            self.__passing.get_total().print_info()
            self.__passing.get_short().print_info()
            self.__passing.get_medium().print_info()
            self.__passing.get_long().print_info()
            self.__passing.get_passing_expected().print_info()
        else: 
            print(None)
        
        if(self.__pass_types != "N/A"):
            self.__pass_types.get_pass_type().print_info()
            self.__pass_types.get_corner_kicks().print_info()
            self.__pass_types.get_outcomes().print_info()
        else: 
            print(None)
        print(f"Goal and Shot Creation: {self.__goal_and_shot_creation}")
        print(f"Defensive Actions: {self.__defensive_actions}")
        print(f"Possession: {self.__possession}")
        print(f"Playing time details: {self.__playing_time_details}")
        print(f"Miscellaneous Stats: {self.__miscellaneous_stats}")
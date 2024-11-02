class  PenaltyKicks:
    __PKatt = "N/A"
    __PKA = "N/A"
    __PKsv = "N/A"
    __PKm = "N/A"
    __Savepercent = "N/A"

    def __init__(self, pk_att="N/A", pka="N/A", pk_sv="N/A", pk_m="N/A", save_percent="N/A"):
        self.__PKatt = pk_att
        self.__PKA = pka
        self.__PKsv = pk_sv
        self.__PKm = pk_m
        self.__Savepercent = save_percent

    def get_pk_att(self):
        return self.__PKatt

    def get_pka(self):
        return self.__PKA

    def get_pk_sv(self):
        return self.__PKsv

    def get_pk_m(self):
        return self.__PKm

    def get_save_percent(self):
        return self.__Savepercent
    
    def print_info(self):
        print(f"Penalty Kicks Attempted (PKatt): {self.__PKatt}")
        print(f"Penalty Kicks Against (PKA): {self.__PKA}")
        print(f"Penalty Kicks Saved (PKsv): {self.__PKsv}")
        print(f"Penalty Kicks Missed (PKm): {self.__PKm}")
        print(f"Save Percentage: {self.__Savepercent}")

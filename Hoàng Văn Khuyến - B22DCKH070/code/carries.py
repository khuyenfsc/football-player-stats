class Carries:
    __carries = "N/A"
    __tot_dist = "N/A"
    __pro_dist = "N/A"
    __prog_c = "N/A"
    __one_third = "N/A"
    __cpa = "N/A"
    __mis = "N/A"
    __dis = "N/A"

    def __init__(self, carries="N/A", tot_dist="N/A", pro_dist="N/A", prog_c="N/A", one_third="N/A", cpa="N/A", mis="N/A", dis="N/A"):
        self.__carries = carries
        self.__tot_dist = tot_dist
        self.__pro_dist = pro_dist
        self.__prog_c = prog_c
        self.__one_third = one_third
        self.__cpa = cpa
        self.__mis = mis
        self.__dis = dis

    def get_carries(self):
        return self.__carries

    def get_tot_dist(self):
        return self.__tot_dist

    def get_pro_dist(self):
        return self.__pro_dist

    def get_prog_c(self):
        return self.__prog_c

    def get_one_third(self):
        return self.__one_third

    def get_cpa(self):
        return self.__cpa

    def get_mis(self):
        return self.__mis

    def get_dis(self):
        return self.__dis
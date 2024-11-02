class ShootingStandard:
    __gls = "N/A"
    __sh = "N/A"
    __sot = "N/A"
    __sot_percent = "N/A"
    __sh_per_90 = "N/A"
    __sot_per_90 = "N/A"
    __g_per_sh = "N/A"
    __g_per_sot = "N/A"
    __dist = "N/A"
    __fk = "N/A"
    __pk = "N/A"
    __pkat = "N/A"

    def __init__(self, gls="N/A", sh="N/A", sot="N/A", sot_percent="N/A", sh_per_90="N/A", sot_per_90="N/A", g_per_sh="N/A", g_per_sot="N/A", dist="N/A", fk="N/A", pk="N/A", pkat="N/A"):
        self.__gls = gls
        self.__sh = sh
        self.__sot = sot
        self.__sot_percent = sot_percent
        self.__sh_per_90 = sh_per_90
        self.__sot_per_90 = sot_per_90
        self.__g_per_sh = g_per_sh
        self.__g_per_sot = g_per_sot
        self.__dist = dist
        self.__fk = fk
        self.__pk = pk
        self.__pkat = pkat


    def get_gls(self):
        return self.__gls

    def get_sh(self):
        return self.__sh

    def get_sot(self):
        return self.__sot

    def get_sot_percent(self):
        return self.__sot_percent

    def get_sh_per_90(self):
        return self.__sh_per_90

    def get_sot_per_90(self):
        return self.__sot_per_90

    def get_g_per_sh(self):
        return self.__g_per_sh

    def get_g_per_sot(self):
        return self.__g_per_sot

    def get_dist(self):
        return self.__dist

    def get_fk(self):
        return self.__fk

    def get_pk(self):
        return self.__pk

    def get_pkat(self):
        return self.__pkat

    def print_info(self):
        print(f"Goals: {self.__gls}")
        print(f"Shots: {self.__sh}")
        print(f"Shots on Target: {self.__sot}")
        print(f"Shots on Target Percentage: {self.__sot_percent}%")
        print(f"Shots per 90 minutes: {self.__sh_per_90}")
        print(f"Shots on Target per 90 minutes: {self.__sot_per_90}")
        print(f"Goals per Shot: {self.__g_per_sh}")
        print(f"Goals per Shot on Target: {self.__g_per_sot}")
        print(f"Average Distance: {self.__dist} meters")
        print(f"Free Kicks: {self.__fk}")
        print(f"Penalties: {self.__pk}")
        print(f"Penalties Attempted: {self.__pkat}")

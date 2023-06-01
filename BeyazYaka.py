
from Calisan import Calisan


class BeyazYaka(Calisan):
    def __init__(self, tc_no,ad, soyad, yas, cinsiyet, uyruk, sektor, maas, tecrube, tesvik_primi):
        super().__init__(tc_no,ad, soyad, yas, cinsiyet, uyruk, sektor, maas,tecrube)
        self.tecrube = tecrube
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, value):
        self.__tesvik_primi = value

    def zam_hakki(self):
        if self.tecrube >= 2 and self.maas <= 15000:
            return (self.maas % self.tecrube) * 5 + self.__tesvik_primi
        elif self.tecrube > 4 and self.maas <= 25000:
            return (self.maas % self.tecrube) * 4 + self.__tesvik_primi
        elif self.tecrube >= 2:
            return self.__tesvik_primi
        else:
            return 0

    def __str__(self):
        return f"{super().__str__()}\nTeşvik Prim: {self.__tesvik_primi}\nZam Hakkı: {self.zam_hakki()}"



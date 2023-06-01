
from Calisan import Calisan


class MaviYaka(Calisan):

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, maas, tecrübe,yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk,sektor,maas,tecrübe)
        self.sektor = sektor
        self.maas = maas
        self.tecrübe = tecrübe
        self.yipranma_payi=yipranma_payi

    def zam_hakki(self):
        if self.tecrübe >= 2 and self.maas <= 15000:
            return (self.maas % self.tecrübe) / 2 + (self.yipranma_payi * 10)
        elif self.tecrübe > 4 and self.maas <= 25000:
            return (self.maas % self.tecrübe) / 3 + (self.yipranma_payi * 10)
        elif self.tecrübe >= 2:
            return self.yipranma_payi * 10
        else:
            return 0

    def __str__(self):
        return f"{super().__str__()}\nYıpranma Payı: {self.yipranma_payi}\nZam Hakkı: {self.zam_hakki()}"



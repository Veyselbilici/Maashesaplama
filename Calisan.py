
from Insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no,ad, soyad, yas, cinsiyet, uyruk, sektor, maas,tecrübe):
        super().__init__(tc_no,ad, soyad, yas, cinsiyet, uyruk)
        self.sektor = sektor
        self.maas = maas
        self.tecrübe=tecrübe

    def __str__(self):
        return f"{super().__str__()}\nSektör: {self.sektor}\nMaaş: {self.maas}\nTecrübe: {self.tecrübe}"



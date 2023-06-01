
class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.tc_no = tc_no
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.uyruk = uyruk

    def __str__(self):
        return f"TC No: {self.tc_no}\nAd: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yas}\nCinsiyet: {self.cinsiyet}\nUyruk: {self.uyruk}"


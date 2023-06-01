from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

# İnsan sınıfı için nesneler oluşturup ve  bu bilgileri yazdırma
insan1 = Insan("12345678901", "Ayşe", "Demir", 30, "Kadın", "Türk")
insan2 = Insan("98765432109", "Mustafa", "Kara", 35, "Erkek", "Türk")
print(insan1)
print(insan2)
print("**********************")

# İşsiz sınıfı için nesneler  ve bilgileri yazdırma işlemi
issiz1 = Issiz("12345678901", "Ayşe", "Demir", 30, "Kadın", "Türk", "Bilişim",5 )
issiz2 = Issiz("98765432109", "Mustafa", "Kara", 35, "Erkek", "Türk", "Pazarlama",3 )
issiz3 = Issiz("74125896302", "Gizem", "Yılmaz", 28, "Kadın", "Türk", "Finans", 7)
print(issiz1)
print(issiz2)
print(issiz3)
print("***-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*****")
# Çalışan sınıfı için de nesneler oluşturup  ve bilgileri yazdırma işlemi uyguluyoruz
calisan1 = Calisan("12345678901", "Ayşe", "Demir", 30, "Kadın", "Türk", "Bilişim", 20000, 2)
calisan2 = Calisan("98765432109", "Mustafa", "Kara", 35, "Erkek", "Türk", "Pazarlama", 25000, 4)
calisan3 = Calisan("74125896302", "Gizem", "Yılmaz", 28, "Kadın", "Türk", "Finans", 18000, 5)
print(calisan1)
print(calisan2)
print(calisan3)
print("*/*/*/*/***//**/*//***//**********/////*/*/*/*/*////****")

# Mavi Yaka sınıfı için nesneler oluşturma ve bilgileri yazdırıyoruz
maviyaka1 = MaviYaka("12345678901", "Emre", "Aksoy", 32, "Erkek", "Türk", "Üretim", 5000, 2, 0.2)
maviyaka2 = MaviYaka("98765432109", "Ayşe", "Kılıç", 30, "Kadın", "Türk", "Lojistik", 4000, 3, 0.5)
maviyaka3 = MaviYaka("74125896302", "Mehmet", "Demir", 35, "Erkek", "Türk", "Enerji", 4500, 4, 0.2)
print(maviyaka1)
print(maviyaka2)
print(maviyaka3)
print("*+++++*++*+*+********+++++++++++++************+*+*+*******")

# Beyaz Yaka sınıfı için nesneler oluşturma ve bilgileri yazdırma
beyazyaka1 = BeyazYaka("12345678901", "Ahmet", "Yılmaz", 30, "Erkek", "Türk", "Muhasebe", 15000, 2, 500)
beyazyaka2 = BeyazYaka("98765432109", "Ayşe", "Kara", 35, "Kadın", "Türk", "İnsan Kaynakları", 20000, 3, 1000)
beyazyaka3 = BeyazYaka("74125896302", "Ali", "Öztürk", 28, "Erkek", "Türk", "Pazarlama", 18000, 5, 2000)
print(beyazyaka1)
print(beyazyaka2)
print(beyazyaka3)
print("****-*-*-*--****-*-**-***--*****--******--****-*******----*-*-**-*******")

# DataFrame oluşturma
data = {
    "Nesne Türü": ["İnsan", "İnsan", "İşsiz", "İşsiz", "İşsiz", "Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
    "TC No": ["12345678901", "98765432109", "12345678901", "98765432109", "74125896302", "12345678901", "98765432109", "74125896302", "12345678901", "98765432109", "74125896302", "12345678901", "98765432109", "74125896302"],
    "Ad": ["Ayşe", "Mustafa", "Ayşe", "Mustafa", "Gizem", "Ayşe", "Mustafa", "Gizem", "Emre", "Ayşe", "Mehmet", "Ahmet", "Ayşe", "Ali"],
    "Soyad": ["Demir", "Kara", "Demir", "Kara", "Yılmaz", "Demir", "Kara", "Yılmaz", "Aksoy", "Kılıç", "Demir", "Yılmaz", "Kara", "Öztürk"],
    "Yaş": [30, 35, 30, 35, 28, 30, 35, 28, 32, 30, 35, 30, 35, 28],
    "Cinsiyet": ["Kadın", "Erkek", "Kadın", "Erkek", "Kadın", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Erkek", "Kadın", "Erkek"],
    "Uyruk": ["Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk", "Türk"],
    "Sektör": ["", "", "Bilişim", "Pazarlama", "Finans", "Bilişim", "Pazarlama", "Finans", "Üretim", "Lojistik", "Enerji", "Muhasebe", "İnsan Kaynakları", "Pazarlama"],
    "Maaş": [0, 0, 0, 0, 0, 20000, 25000, 18000, 5000, 4000, 4500, 15000, 20000, 18000],
    "Tecrübe": [0, 0, 0, 0, 0, 2, 4, 5, 2, 3, 4, 2, 3, 5],
    "Yıpranma Payı": [0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0.5, 0.2, 0, 0, 0],
    "Teşvik Prim": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 500, 1000, 2000],
    "Yeni Maaş": [0, 0, 0, 0, 0, 20000, 25000, 18000, 5200, 5200, 5400, 15000, 20000, 18000]
}

df = pd.DataFrame(data)

# a) Boş değerleri 0 ile dolduruyoruz
df.fillna(0, inplace=True)

# b) Gruplandırarak tecrübe ve yeni maaş ortalamalarını hesaplamaya çalışıyoruz
gruplanmis_df = df.groupby("Nesne Türü").agg({"Tecrübe": "mean", "Yeni Maaş": "mean"})
print(gruplanmis_df)

# c) Maaşı 15000TL üzerinde olanların toplam sayısını buluma
maas_ust_limit = 15000
ust_limit_sayisi = df[df["Maaş"] > maas_ust_limit].shape[0]
print("Maaşı 15000TL üzerinde olanların sayısı:", ust_limit_sayisi)

# d) Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama
siralama_df = df.sort_values("Yeni Maaş")
print(siralama_df)

# e) Tecrübesi 3 seneden fazla olan Beyaz yakalıları arayıp bulma
beyazyaka_tecrubesi_3 = df[(df["Nesne Türü"] == "Beyaz Yaka") & (df["Tecrübe"] > 3)]
print(beyazyaka_tecrubesi_3)

# f) Yeni maaşı 10000 TL üzerinde olanların tc_no ve yeni_maaş sütunlarını  seçme
yuksek_maasli_df = df[df["Yeni Maaş"] > 10000][["TC No", "Yeni Maaş"]]
print(yuksek_maasli_df.head(5))

# g) Ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame oluşturup elde etmeS
yeni_df = df[["Ad", "Soyad","Sektör", "Yeni Maaş"]]
print(yeni_df)

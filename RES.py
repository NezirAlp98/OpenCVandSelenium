import matplotlib.pyplot as plt
data = {
    "Aydın": 414,
    "Balıkesir": 1135,
    "Denizli": 306,
    "İzmir": 1462.2,
    "Manisa": 669.95,
    "Muğla": 414,
    "Uşak": 306,
    "Tekirdağ": 228.5,
    "Edirne": 78,
    "Kırklareli": 78,
    "İstanbul": 78,
    "Bursa": 78,
    "Balıkesir": 78,
    "Çanakkale": 505.6,
    "Sakarya": 78,
    "Yalova": 78,
    "Kocaeli": 78
}
labels = list(data.keys())
values = list(data.values())

plt.bar(labels, values,color='green')

# Grafiğin eksenlerini ve başlığını belirleyelim
plt.xlabel("Şehir")
plt.ylabel("Kurulu Güç (MW)")
plt.title("Türkiye'deki RES'lerin Şehirlere Göre Kurulu Güç Dağılımı")

# Grafiği gösterelim
plt.show()
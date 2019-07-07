kaynak = "şçöğüıŞÇÖĞÜİ"
hedef =  "scoguiSCOGUI"

ceviri_tablosu = str.maketrans(kaynak,hedef)
print(ceviri_tablosu)

metin = "bilge adam bireysel eğitimlerde artık python dersleri başlayacaktır"
print(metin)
metin = metin.translate(ceviri_tablosu)
print(metin)

#{351: 115, 231: 99, 246: 111, 287: 103, 252: 117, 305: 105, 350: 83, 199: 67, 214: 79, 286: 71, 220: 85, 304: 73}
#bilge adam bireysel eğitimlerde artık python dersleri başlayacaktır
#bilge adam bireysel egitimlerde artik python dersleri baslayacaktir
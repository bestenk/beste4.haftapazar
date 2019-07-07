# .count metin yada dizi içerisinde parametrede verilen değerin adet bilgisini teslim eder.

metin = "bilge adam beşiktaş"
sonuc = metin.count("b")
print("metin içerisinde toplamda verdiğiniz parametre {} adet içermektedir".format(sonuc))


metinler = ["ankara","edirne","istanbul","ankara","eskişehir"]

result = metinler.count("ankara")
print(result)

metin = "beste karademir"
sonuc = metinler.count("e")
print(sonuc)
sonuc = metin.count("e",4) #4.parametrede verilen değer başlangıç index değeridir arama işlemine 2.indexten başla
print(sonuc)

metin = "bilge adam beşiktaş yazılım dersleri klima ön tarafı soğutmasada arkada kış ayları estirmektedir"
sonuc = metin.count('a')
print("toplam a karakterleri  :",sonuc)
sonuc = metin.count('a',6,20)
print("toplam a karakterleri  :",sonuc)
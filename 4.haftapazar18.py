#  .index(), .rindex()

metin = "beste karademir bilge adam beşiktaş yazlım"
sonuc = metin.index('a') # verilen karakteri metin içerisinde soldan sağa doğru arama işlemi yapar eğer belirtilen karakter metin içerisinde var ise index değerini yok ise hata döner
print(sonuc)

sonuc = metin.rindex("a") # # verilen karakteri metin içerisinde sağdan sola doğru arama işlemi yapar eğer belirtilen karakter metin içerisinde var ise index değerini yok ise hata döner

####################################################

# .find(), .rfind()

metin = "beste karademir bilge adam beşiktaş yazlım"
sonuc = metin.find('a') # verilen karakteri metin içerisinde soldan sağa doğru arama işlemi yapar eğer belirtilen karakter metin içerisinde var ise index değerini yok ise -1 döner
print(sonuc)

sonuc = metin.rfind("a") # # verilen karakteri metin içerisinde sağdan sola doğru arama işlemi yapar eğer belirtilen karakter metin içerisinde var ise index değerini yok ise -1 döner
# .capitalize() => parametrede verilen değerin ilk harfini büyük olarak değiştirir

isim = "beste karademir".capitalize()


print(isim.capitalize())
# title() => metin içerisinde yer alan tüm ayrık kelimelerin ilk harfini büyük olarak teslim eder.
print(isim.title())

# Beste Karademir

#############################################################################

# .sorted() => dizi içerisinde yer alan elemanları A'dan z'ye, 0'dan 9'a sıralama yapar.

sonuc = sorted("bilgeadam")
print(sonuc)

# ['a','a','b','e'...]
#alfebatik sıraya göre değil ascii kod üzerinden devam eder düzeltmek için

import locale
# locale.setlocale(locale.LC_ALL,"Turkısh_Turkey.1254") #windows için
# locale.setlocale(locale.LC_ALL"tr_TR") #GNU\Lİnux için



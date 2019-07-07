# .center() => nesneye uygulandığında soldan ve sağdan eşit boşluklar verir

# NOT : METNİN KARAKTER UZUNLUĞUNU VERİLEN DEĞERDEN ÇIKARTIR VE KALAN DEĞERİ BOŞLUK OLARAK SOLA VE SAĞA DAĞITIR

metin = "bilge adam"
print(len(metin))
metin = metin.center(15)
print(metin)
print(len(metin))
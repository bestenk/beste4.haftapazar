# .swapcase() => metin içerisinde yer alan büyük karakterleri küçük, küçük karakterleri ise büyük harfe çevirir

#metin = "Bilge Adam"

#print(metin.swapcase())
#bILGE aDAM

############################################################

# .strip() => metin bşındaki veya sonundaki karakteri silmek için kullanılır.
#metin = " bilge adam "
#print(metin)
#print(len(metin))

#metin = metin.strip(" ")  # sağdaki ve soldaki boşlukları siler
#print(metin)
#print(len(metin))

#metin = " bilge adam"
#metin = metin.strip()  # soldaki boşluğu siler
#print(len(metin))

#metin = " bilge adam"
#metin = metin.rsplit() #sağdaki boşluğu siler
#print(metin)

#############################################################

# .join metinsel değerleri birbirine eklemek için kullanılır seperator de denilebilir.

metin = list(input("lütfen metin giriniz :"))

print("-".join(metin))
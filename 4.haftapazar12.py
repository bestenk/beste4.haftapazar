metin = "bilge adam BEŞİKTAŞ"
print(metin.lower()) #küçük harfe çevirir
print(metin.upper()) # büyük harfe çevirir


#bilge adam beşi̇ktaş
#BILGE ADAM BEŞİKTAŞ


metin = metin.lower()
result = metin.islower()  # tüm karakterlerin küçük olup olmadığını kontrol eder
print(result)

result = metin.isupper()  # karakterlerin büyük olup olmadığını kontrol eder
print(result)
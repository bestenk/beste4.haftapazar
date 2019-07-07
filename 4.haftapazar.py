# dışarıdan gelecek olan parametre sayısı belirsiz olan durumlar için kullanılan metot örneği

#  c# params

def hesapla (*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam

result = hesapla(1,2,3,4,5,6,7,8,9,10,11,12,13)
print(result)
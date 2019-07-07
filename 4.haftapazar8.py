# dışardan girilen metin içerisinde yer alan tüm karakterlerin ascii kod değerlerinin toplamını bulunuz

metin = input("lütfen bir metin giriniz")
def metintoplamdeğer(string):
    havuz = 0
    liste = list(string)
    for i in liste :
        havuz += ord(i)
    return havuz
result = metintoplamdeğer(metin)
print(result)
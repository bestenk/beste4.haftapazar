# metot(ad,soyad,telefon,gorev)
# metot(*parametreler):

def metot(ad, soyad, telefon, gorev):
    print(ad, soyad, telefon, gorev)


def metot1(*params):
    for i in params:
        print(i)

metot("beste","karademir","34567897","öğrenci")


def metotvol1(**params):
    print(params["ad"])
metotvol1(ad="beste karademir",soyad= "karademir",telefon="378289529")
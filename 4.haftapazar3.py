def kayitlar(**params):
    print("-"*25)
    for key,value in params.items():
        print("{0:<8}: {1}".format(key,value))
    print("-"*25)
kayitlar(
    ad      ="beste",
    soyad   ="karademir",
    telefon ="939378529",
    mail    ="besteekarademir@gmail.com")


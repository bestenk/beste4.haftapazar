# .splitlines() => her bir alt satırdaki elemanların aralarına [,] karakteri ekler
# not : metin altta yer alan örnek gibi yazıldıysa geçerlidir.

metin = """bilge
adam
yazılım
python
dersleri
"""
print(metin.splitlines())

print(metin.splitlines(True))

# ['bilge', 'adam', 'yazılım', 'python', 'dersleri']
# ['bilge\n', 'adam\n', 'yazılım\n', 'python\n', 'dersleri\n']

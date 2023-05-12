# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")
texto = arquivo.read()
print(texto)

#operacoes de write
w = open("arquivo2.txt", "w")
w.write("File 2 olá")
w.close()
arquivo2 = open("arquivo2.txt")
r = arquivo2.read()
print(r)

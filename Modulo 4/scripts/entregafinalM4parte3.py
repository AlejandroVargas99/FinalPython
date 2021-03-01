#MODULO4-PROBLEMA 1
import pandas as pd
adn = pd.read_csv("./data/dna/databases/large.csv")
# MODULO4-PROBLEMAS DIVERSOS
# 1y2
import os
valortexto=""
numero = int(input('Introduzca un número del 1 al 10'))
with open("./tabla-n.txt",mode="w+") as f:
    for u in range (1,10):
        valor = numero*u
        valortexto = str(valor)
        f.write(valortexto)
        datos=f.readlines()
        print(datos)
    for linea in f:
        print(f)
    f.close()
#MODULO4-PROBLEMAS DIVERSOS
#EXPRESIONES REGULARES
#1
import re
s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
re.findall('@robot9',s)
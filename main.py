import os
import pandas as pnd
pnd.set_option('display.max_columns',None)
listaDeArchivos=os.listdir("datas")
for archivo in listaDeArchivos:
    print(archivo)

nuestrosPokemon=pnd.read_csv("database/pokemon"
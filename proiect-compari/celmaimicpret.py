import json

path = "/home/radu/Projects/workspace/proiect-compari"

with open(f"{path}/anunturi.json") as f:
    dictionar = json.load(f)

listapret = dictionar['pret']
listatitlu = dictionar['titlu']
listasite = dictionar['site']

min1 = listapret[0]
nr = 0
for i in range(len(listapret)):
    # If the other element is min than first element
    if listapret[i] < min1: 
        min1 = listapret[i] #It will change
        nr = i
print(f"Cel mai mic pret este, {min1}\nSi este vandut de catre {listasite[nr]}")
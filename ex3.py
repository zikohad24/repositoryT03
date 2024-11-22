"""
Utilitza un bucle while per girar una cadena: Entrada “ABCDE” sortida “EDCBA”
"""
lletres="ABCDE" #creem una cadena
lletres_invertida="" #creem una cadena buida

indice = len(lletres)-1 #aixó es fa per saber la última lletra, per aixó utilitzem "-1"
while indice>=0: #per a que el bucle segueixi, ja que es mes gran o igual que 0
    lletres_invertida += lletres [indice]
    indice -= 1 #per seguir a la següent lletra

print(lletres_invertida) #demanen que en retorni la cadena invertida
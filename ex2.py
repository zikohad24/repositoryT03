"""
2. Donat un string que introdueix lusuari per teclat, imprimeix-lo igual però sense vocals.
 Recorda que cal utilitzar un bucle while.
"""
vocals="aeiouAEIOU"
i = 0
nova_frase=""
frase = input("Introdueix una frase: ")  #primer demanen una frase
while i < len(frase):  #demanen que recorri tota la frase
    if frase[i] in vocals: #demana venure si es una consonant o no
        pass #utilitzat per passar si es vocal
    else:
        nova_frase += frase [i] #aqui demanen que si no es vocal, s'afegeix a la nova frase
    
    i += 1
    
print ("Frase sense vocals:", nova_frase) #demana que en retorni la frase sense vocals

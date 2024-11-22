"""
1.Fes un programa que vagi demanant números per teclat fins que introduïm 
un número negatiu i mostri per pantalla, per cada número entrat, si és parell o és senar.
El programa deixa de  demanar números quan introdueix un nombre negatiu. 
Finalment ens mostrarà quants nombres han introduït, i aquests quants són parells i quants senars. 
A més calcula la suma de tots els nombres, de tots els nombres parells i de tots els senars.
"""

total_senars=0 #comptador dels senars
total_parells=0 #comptador dels parells
suma_total=0 
num=0 #per identificar el número
contador=0 

while num>= 0:
    num=int(input("Introdueix un numero: ")) #demanem que s'introduï un número
    if num>=0: #seguir la seqüencia sempre que sigui positiu
        contador+=1
        suma_total += num
        if num %2 ==0: #aquest "if" és per coneixe si el nombre es parell
            total_parells += num
            print("El número", num, "és parell")
        else: #aquest "else" és per coneixe si el nombre es senar
            total_senars += num
            print("El número", num, "és senar")

print("\nTotal de números introduïts:", contador)
print("Suma total de tots els nombres:", suma_total)
print("Suma total de tots els nombres parells:", total_parells)
print("Suma total de tots els nombres senars:", total_senars)

#per fer retorn de l'informació
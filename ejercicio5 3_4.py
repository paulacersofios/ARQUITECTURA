frutas = ["Manzana", "Pera", "Uva", "Mandarina"]
frutas.append("banana")
print(frutas[1])

frutas.insert(2, "durazno")
frutas.remove("Uva")
frutas.sort()
frutas.reverse()
for fruta in frutas:
    print(fruta)
    


contador=0
while contador == 5:
    print(contador)
    contador +=1



contador=0
while contador <= 10:
    
    contador +=1
    print(contador)


suma=0
valor=int(input("ingrese un valor:"))
while valor !=0:
    suma=suma+valor
    valor=int(input("inserte un valor"))
print(f"el total es {suma}")

# #Imprimir “Hello world” per pantalla.
# msg = 'Hello world'
# print(msg)




# # Demanar a l’usuari que introdueixi 2 valors numèrics i mostrar, per pantalla, la suma dels dos valors i quin és el més gran.
# n1 = int(input("Ingresa un valor: "))
# n2 = int(input("Ingresa otro valor: "))
# print("El resultado de la suma es:", n1 + n2)




# Demanar a l’usuari que introdueixi una frase i imprimir-la per pantalla sense espais en blanc. 
# msg = input("introduce una frase:  ")
# sinEspacios = msg.replace(" ","") # Las primeras comillas -> " " hacen referencia a lo que quiero remplazar en la cadena
# print(sinEspacios)




# # Mostrar els números imparells de l’1 al 500 a través d’algun loop.
# for i in range(500+1):
#     resultado = i % 2
#     if resultado == 1:
#         print(i)




# # Demanar a l’usuari que introdueixi un valor decimal (en €),
# # seguidament demanar que introdueixi el IVA a aplicar-hi (4, 10 o 21%) i finalment mostrar per pantalla, 
# # el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit.
# valor = float(input("ingrese un valor decimal (€):  "))
# iva = int(input("ingrese el IVA a aplicar (4%, 10%, 21%):  "))
# if iva == 4:
#     resultado = valor*1.04
#     redondeo = round(resultado,2)
#     print("Precio: ", valor,"€", "\nIVA: ",  iva,"%", "\nEl precio con IVA es: ", redondeo,"€")
# elif iva == 10:
#     resultado = valor*1.10
#     redondeo = round(resultado,2)
#     print("Precio: ", valor,"€","\nIVA: ",  iva,"%",  "\nEl precio con IVA es: ", redondeo,"€")
# elif iva == 21:
#     resultado = valor*1.21
#     redondeo = round(resultado,2)
#     print("Precio: ", valor,"€", "\nIVA: ",  iva,"%",  "\nEl precio con IVA es: ", redondeo,"€")





# Demanar a l’usuari que posi entre 2 i 3 paraules. A l’executar el programa, mostrarà les paraules indicades per l’usuari, 
# indicar quants caràcters té i indicar el primer, i l’últim caràcter.
smg = input("ingresa aqui de 2 a 3 paraules: ")
numCaracter = len(smg)
primerC = smg[0]
ultimoC = smg[numCaracter-1]
print("Has ingresado ",smg, "\nLa logitud es ", numCaracter, "\nLa primera letra es: ",primerC,"\nLa ultima letra es: ", ultimoC)





# Demanar a l’usuari que posi una paraula o una frase i que el programa ens indiqui si és capicua (Palíndrom). Ex: Anna, Llull, caiac, mínim,...

# Desenvolupar un programa que primerament esculli aleatòriament un número entre 1 i 100. Després l’usuari haurà d’anar afegint un número fins que l’encerti. 
# Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran.
# Un cop l’encerti caldrà d’indicar que l’ha encertat i mostrar el número d’intents.




# LLISTES, TUPLES I DICCIONARIS

# Posa un exemple d'una llista, d’una tupla i d’un diccionari i explicar les diferències.

# Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla el mes corresponent al número indicat per l’usuari. 

# Demanar a l’usuari que introdueixi 10 números separats per un espai. A l’acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com vulgueu), mostrant per pantalla el contingut de la tupla.

# Demanar 10 cops una paraula diferent a l’usuari. 
# Cada paraula que l’usuari introdueix es guardarà en una llista i es mostrarà per pantalla tota la llista ordenada alfabèticament.

# Demanar a l’usuari posar 2 paraules. Afegir aquestes a una llista i mostrar per pantalla quantes vegades apareix cada lletra.

# Cal buscar la informació que es demana de la següent list:
# areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
# (Cal utilitzar els “:” per a que siguin vàlids els prints següents)
# Imprimir el segon element
# Imprimir l’últim element
# Imprimir l’àrea de la terrassa
# Imprimir del primer element al tercer element
# Imprimir del tercer element a l’últim
# Imprimir el total de l'àrea de les dues habitacions
# Modificar l’àrea del lavabo i imprimir la nova list area
# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
# Imprimir el total de l’àrea del pis.

# Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. S’haura de demanar a l’usuari que posi contactes (noms i edats). Si algun nom es repeteix no s'afegeix al diccionari (indicant-ho a l’usuari). Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista. Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.

# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:

# Demanar a l’usuari que posi 5 números separats per un espai. Afegir aquest números en una llista i retornar la suma més gran entre 2 números contigus (que estiguin un al costat de l’altre)

# —--------------------------------------------------------------------------------------------------------------------------------

# Funcions
# Crear una funció que sumi dos números passats per paràmetre. Aquests números seran demanats a l’usuari. 
# (En aquest cas haurieu de tindre un arxiu on feu el càlcul de dos números passats per paràmetre i un arxiu main.py on trucarà aquesta funció i li passarà els números indicats per l’usuari.)

# Crear una funció que passats dos números per paràmetre (demanats a l’usuari) ens mostra per pantalla tots els números (enters) que hi ha entre ells. També mostrarà per pantalla la suma d’aquests números enters.

# Crear una funció que passat un nom per l’usuari (nom). Mostri per pantalla “Hola nom”.

# Crear una funció per calcular el total d’una factura amb l’IVA. La funció ha de rebre (per paràmetre) la quantitat sense IVA i l’IVA a aplicar (introduïts per l’usuari). En cas de no passar-li cap valor o un valor erroni (4%, 10% o 21%) s’aplicarà directament el 21%. Es mostra per pantalla el valor sense IVA, l’IVA i el total.

# Crear una funció que agafi una llista amb 10 números, i retorni una altra llista amb els seus quadrats.

# —--------------------------------------------------------------------------------------------------------------------------------

# PROGRAMACIÓ FUNCIONAL

# Crear una funció que rebi un diccionari amb una llista de la compra (amb preus i descomptes).
# Exemple llista compra: {100:10, 250:5, 1500:30, …}
# on 100 és el preu i 20 el descompte a aplicar a aquests 100.
# Demanar a l’usuari l’IVA a aplicar al total de la llista de la compra.
# Mostrar per pantalla els valors amb el descompte aplicat més l’IVA.
# Exemple:
# Producte 1: 
# Producte 2: 
# …

# Crear una funció que rebi una frase per paràmetre. Aquesta frase es demana a l’usuari. Ha de retornar un diccionari amb les paraules que conté i la longitud de cada paraula.

# XML I JSON

# Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
# Un root de nom students.
# Cinc childs (del root) amb nom student.
# Cada child student ha de tindre 4 subchilds:
#  name
#  surname
#  email
#  dni
# Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
# El text de cada etiqueta serà de la vostra elecció.


# —--------------------------------------------------------------------------------------------------------------------------------

# Classes i objectes

# Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
# Constructor
# Atributs (mínim 6)
# Getters/Setters
# Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
# Afegir el mètode to_dict(self) a la classe per retornar l’objecte en format json




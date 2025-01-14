#Declaración de los datos
taza=1
cucharada= taza*16
cucharadita= cucharada*3
coccion= 0.9

#Explicación del procedimiento
print("Para preparar una masa de arepas, se mezcla en proporciones iguales la harina y el agua, añadiendo cucharadas de aceite y sal a la mezcla")
print("¿Cuál es la cantidad de ingredientes que tiene?")

#Definir variables
tzadeagua=float(input("Cantidad de tazas de agua: "))
tzaharina= float(input("Cantidad tazas de harina: "))
cdtasal= float(input("Cantidad de cucharaditas de sal: "))
cdtaaceite= float(input("Cantidad de cucharaditas de aceite: "))

#Conversión de unidades
cdaagua= tzadeagua*cucharada
cdadeharina= tzaharina*cucharada
cdtaagua= tzadeagua*cucharadita
cdtaharina= tzaharina*cucharadita

if tzadeagua <= tzaharina:
    agvolumenprecda= cdaagua*2+cdtasal/3+cdtaaceite/3
    agvolumenprecdta= cdtaagua*2+cdtasal+cdtaaceite
    agvolumenfinalcda= agvolumenprecda*coccion
    agvolumenfinalcdta= agvolumenprecdta*coccion
    print("El volumen tras la cocción de la arepa en cucharadas es de", agvolumenfinalcda)
    print("El volumen tras la cocción de la arepa en cucharaditas es de", agvolumenfinalcdta)
elif tzadeagua >= tzaharina:
    havolumenprecda= cdadeharina*2+cdtasal/3+cdtaaceite/3
    havolumenprecdta= cdtaharina*2+cdtasal+cdtaaceite
    havolumenfinalcda= havolumenprecda*coccion
    havolumenfinalcdta= havolumenprecdta*coccion
    print("El volumen tras la cocción de la arepa en cucharadas es de", havolumenfinalcda)
    print("El volumen tras la cocción de la arepa en cucharaditas es de", havolumenfinalcdta)

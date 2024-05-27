def pesopino(altura):
    if (altura > 3):
        peso = 3 * 3 + (altura - 3) * 2
    else:
        peso = altura * 2
    return peso

def es_peso_util(peso):
    if (peso > 400 and peso < 1000):
        return True
    else:
        return False

def sirvepino(altura):
    if (es_peso_util(pesopino(altura))):
        return True
    else:
        return False

def uno_diez():
    i = 1;
    while (i<=10):
        print(i)
        i += 1


def pares_uno_diez():
    i = 2;
    while (i<=10):
        print(i)
        i += 2

#pares_uno_diez();

def eco_uno_diez():
    i = 1;
    while (i<=10):
        print("eco")
        i += 1

#eco_uno_diez();


def reemplazar_pares(lista):
    nueva_lista = []
    i = 0
    while i< len(lista):
        if (i%2==0):
            nueva_lista.append("0")
        else:
            nueva_lista.append(lista[i])
        i +=1;
    return nueva_lista;

#print(reemplazar_pares([1,1,1,1,1,1,1,]))

def reemplazar_pares_mismalista(lista):
    i = 0
    while i< len(lista):
        if (i%2==0):
            lista[i] = 0
        i += 1;
    return lista;

#print(reemplazar_pares_mismalista([1,1,1,1,1,1,1,]))

def borrarVocales(lista):
    nueva_lista = []
    for i in lista:
        upperi = str.upper(i)
        if (upperi != "A" and upperi!="E" and upperi!="I" and upperi!="O" and upperi!="U"):
            nueva_lista.append(i)
    return nueva_lista

#print(borrarVocales("abCDEFG"))

def darvuelta(palabra):
    nuevostr = ""
    return palabra;
    

def eliminar_repetidos(palabra):
    nuevaPalabra = [];

    i = 0
    while i < len(palabra):
        ii = i + 1;
        seRepite = False;

        while ii < len(palabra):
            if (palabra[i] == palabra[ii]):
                seRepite = True
            ii += 1

        if (seRepite == False):
            nuevaPalabra.append(palabra[i]);

        i+=1;

    return nuevaPalabra;

#print(eliminar_repetidos("holahola"))



def aprobado(notas):
    for i in notas:
        if (i < 4):
            return 3;
    
    if (promedioNotas(notas) < 4):
        return 3
    elif (promedioNotas(notas) > 4 and promedioNotas(notas) < 7):
        return 2
    elif (promedioNotas(notas) > 7): return 7


def promedioNotas(notas):
    sumaNotas = 0;
    for i in notas:
        sumaNotas += i

    return sumaNotas / len(notas)

#print(promedioNotas([4,4,4,10,10,10,4,4]))
#print(aprobado([4,4,4,10,10,10,4,4]))

def pertenece_a_cada_uno_v2(seq, num):
    res = [];
    for i in seq:
        if (num == i[0] or num == i[1]):
            res.append(True);
        else: res.append(False);
    return res;

#print(pertenece_a_cada_uno_v2([(4,0),(4,0),(4,0),(3,0)], 4))
lista_nombres = [];

def nombres():
    nom = input("ingrese nombre");
    if (nom == "listo"):
        return lista_nombres
    else:
        lista_nombres.append(nom)
        nombres();
        

nombres();
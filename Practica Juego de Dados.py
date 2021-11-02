import random
resultados=[]


def comparacion(resultados):
    mayor=max(resultados)
    if resultados.count(mayor)==1:
        print("\n El ganador es el jugador # ", resultados.index(mayor)+1)
        print("\n Resumen del juego:")
        j=0
        for r in resultados:
            j=j+1
            print("\n El jugador {} obtuvó {}".format(j,r))
        print("\n Gracias por participar")
    else:
        print("\n Los siguientes jugadores empataron con {} puntos: ".format(mayor))
        pos_covered=0
        jug_desempate=resultados.count(mayor)
        while pos_covered<len(resultados):
            posicion=resultados.index(mayor,pos_covered)
            print("\n Jugador {}".format(posicion+1))
            pos_covered=posicion+1

        print("\n Se requiere jugar un desempate entre los jugadores")
        juego_principal(jug_desempate,resultados=[])

def juego_principal(n,resultados):
    i=0

    while i<n:
        print("\n Turno del jugador", i+1)
        x=input("Por favor presione enter para tirar el dado: ")
        if x=="":
            resultados.insert(i,random.randint(1,6))
            print("\n El resultado del jugador", i+1, "es", resultados[i])

        i=i+1

    comparacion(resultados)
    return(resultados)


print("\t Practica - Juego de Dados")

print("\n\t Bienvenido al juego de dados")

print("\n Instrucciones:")

print("\n Cada jugador tirará los dados una vez; el mayor número ganará.")

print("\n En caso de empate, se debe jugar una ronda de desempate")

n=int(input("\n Por favor indicar el número de jugadores que van a participar: "))

juego_principal(n,resultados)




    

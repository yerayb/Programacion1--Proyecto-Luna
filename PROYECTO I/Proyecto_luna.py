###Este programa nos calcula la posición de la luna durante
###su órbita alrededor de la Tierra.
###Programa ofrecido por Yeray Bellanco, Jon Uraga y Diego Presa

import math #Importar libreria math nos permitira acceder a funciones matematicas
from tabulate import tabulate #Importar libreria tabulate nos permitira imprimir en la salida estándar un archivo de texto tablas con datos tabulados

#Definir las constantes necesarias

R_tierra = 6371e3
M_luna = 7.348e22
M_tierra = 5.9722e24
G = 6.674e-11

#Funcion que calcula la distancia entre los planetas siendo la diferencia entre los dos planetas
def Calcular_Distancia_Planetas(planeta_1, planeta_2):
    return math.sqrt( (planeta_2[0]- planeta_1[0]) ** 2 + (planeta_2[1] - planeta_1[1]) ** 2)

#Funcion que convierte los dias en segundos
def Calcular_Segundos(dias):
    segundos = dias * 24 * 3600
    return segundos

#Funcion que calcula la formula gravitacional mediante su formula : Fg = -G·M·m/r2 * Ur
#Ur sera la division de la posicion de la luna entre las distancia
#que haya entre los planetas
def Calcular_Fg(distancia_planetas, posicion_luna):
    return  (-(G * M_luna * M_tierra / (distancia_planetas) ** 2) * (posicion_luna[0]/distancia_planetas), -(G * M_luna * M_tierra / (distancia_planetas ** 2) * (posicion_luna[1]/distancia_planetas)))

#Funcion que calcula la velocidad despejando la formula relacionada entre
#la velocidad, el espacio y el tiempo: velocidad = tiempo * aceleracion
def Calcular_Variacion_Velocidad(aceleracion, tiempo):
    return (aceleracion[0] * tiempo, aceleracion[1]* tiempo )

#Funcion que calcula la aceleracion de la luna dividiendo la fuerza sometida
#entre la masa
def Calcular_Aceleracion_Luna(fuerza_gravedad):
    return (fuerza_gravedad[0] / M_luna,fuerza_gravedad[1] / M_luna)

#Funcion que calcula la velocidad de la luna mediante la suma del incremento
#y la velocidad inicial
def Calcular_Velocidad_Luna(velocidad_inicial, variacion_velocidad):
    return (velocidad_inicial[0] + variacion_velocidad[0], velocidad_inicial[1] + variacion_velocidad[1] )

#Funcion que calcula la posicion de la luna siendo : Posicion inicial + (Velocidad actual * tiempo)
def Calcular_Posicion_Luna(posicion_inicial, velocidad_actual, tiempo):
    return (posicion_inicial[0] + velocidad_actual[0] * tiempo , posicion_inicial[1] + velocidad_actual[1] * tiempo )

#Funcion que asegura que el numero introducido sea valido.
def leer_numero(t):
    dato_valido = False
    while not dato_valido:
        try:
            valor = int(input(t))
            if valor >= 0:
                dato_valido = True
            else:
                print("Error. Se esperaba un numero entero positivo")
        except ValueError:
            print("Error. Se esperaba un numero entero,debes introducir un numero entero: ")
    return valor

#Funcion principal
def main():

    posicion_luna = (0.0, 384402e3)
    posicion_tierra = (0.0, 0.0)
    velocidad_tierra = (0.0, 0.0)
    velocidad_luna = (1023.055, 0.0)
    distancia_luna_t = 384402e3
    fuerza_gravedad = Calcular_Fg(distancia_luna_t, posicion_luna)

    l_salida = []
    elemento_salida = []

    #Preguntas que el programa hara al usuario
    tiempo_total = leer_numero("Introduce el tiempo total de simulacion (dias): ")
    incremento_paso_tiempo = leer_numero("Introduce el incremento en cada paso de tiempo (s): ")

    reps = Calcular_Segundos(tiempo_total) / incremento_paso_tiempo

    reps_dia = reps / tiempo_total

    i = 0 #Metemos un contador con valor 0

    elemento_salida = [i * incremento_paso_tiempo, i / reps_dia, fuerza_gravedad, posicion_luna, distancia_luna_t]
    l_salida.append(elemento_salida)

    #bucle mediante contador i que permitira el calculo de posicion
    while i <= reps:
        distancia_luna_t = Calcular_Distancia_Planetas(posicion_tierra, posicion_luna)
        fuerza_gravedad = Calcular_Fg(distancia_luna_t, posicion_luna)
        aceleracion_luna = Calcular_Aceleracion_Luna(fuerza_gravedad)
        cambio_velocidad = Calcular_Variacion_Velocidad(aceleracion_luna, incremento_paso_tiempo)
        velocidad_luna = Calcular_Velocidad_Luna(velocidad_luna,cambio_velocidad)
        posicion_luna = Calcular_Posicion_Luna(posicion_luna,velocidad_luna,incremento_paso_tiempo)

        #En el caso de que el numero de repeticiones de un dia coincide con el numero de calculos listaremos el elemento salida.
        if  i % reps_dia == 0 and i != 0:
            elemento_salida = [i * incremento_paso_tiempo, i / reps_dia, fuerza_gravedad, posicion_luna, distancia_luna_t]
            l_salida.append(elemento_salida)

        i += 1 #Incrementamos 1 el contador
    print(tabulate(l_salida, headers = ['t (s)', 't (d)', 'F (N)', '(x, y) (m)', 'R (m)']))

if __name__ == '__main__':
    main ()

###Programa finalizado.

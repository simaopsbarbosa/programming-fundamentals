import math

def time_until_lost_connection(direction_A, direction_B):
    alfa = abs(direction_A - direction_B)
    beta = abs((180 - alfa) / 2)

    # distancia está em km
    distancia = abs((35 * math.sin(math.radians(beta))) /
                    math.sin(math.radians(alfa)))

    if distancia == 0:
        distancia = 35 / 2

    # velocidade é 5 hm / 60 min
    tempo = round((60 * distancia) / 5, 3)
    return tempo

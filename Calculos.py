from random import getrandbits, randint, random, choice
import sys
import os

#Se generan los individuos
def generate_individual(n_items):
    return [ getrandbits(1) for x in range(n_items) ]
    
#Se generan la población total
def generate_population(n_individuos , n_items):
    return [ generate_individual(n_items) for x in range(n_individuos)]


def fitness(individuo, cal_maximas, pesos_valores):
    peso_calorias, valor_proteina , valor_grasa , valor_car = 0, 0 , 0, 0
    
    for indice, valor in enumerate(individuo):
        #calorias , proteinas , grasas , carbohidratos
        peso_calorias += (individuo[indice] * pesos_valores[indice][0])        #multiplica el valor del individuo x lo que hay en esa posición
        valor_proteina += (individuo[indice] * pesos_valores[indice][1])       #valor
        valor_grasa += (individuo[indice] * pesos_valores[indice][2])
        valor_car += (individuo[indice] * pesos_valores[indice][3])

    carbohidratos = (peso_calorias * 10) / 100
    proteinas = (peso_calorias * 20) / 100
    grasas = (peso_calorias * 75) / 100 

    if (cal_maximas - peso_calorias) < 0:
        return -1 #Retorna -1 en caso de exceso de peso (calorias)

    if (valor_car > carbohidratos) or (valor_car > 50):
        return -1   #Retorna -1, en caso de que los carbohidratos sean mayores al 15%

    if (valor_proteina > proteinas):
        return -1
    
    if (valor_grasa > grasas):
        return -1

    return peso_calorias #si es un individuo válido, devuelve su valor.


def media_fitness(poblacion, cal_maximas, pesos_valores): #solo tiene en cuenta los elementos que respetan el peso máximo de la mochila
    summed_cal = 0
    for x in poblacion:
        resultado = fitness (x , cal_maximas , pesos_valores)
        if resultado >= 0:
            summed_cal = summed_cal + resultado

    promed = summed_cal / (len(poblacion) * 1.0)
    return promed


def selection(poblacion, cal_maximas, pesos_valores, n_cromosomas, mutate=0.05): 
    best_aptos = []
    for x in poblacion:
        resultado = fitness(x, cal_maximas, pesos_valores)
        if resultado >=0:
            best_aptos.append([resultado , x])
    
    best_aptos.sort(reverse=True)

    # Reproducción
    hijos = []
    while len(hijos) < n_cromosomas:
        padre1, padre2 = metodo_ruleta(best_aptos)
        aux_operacion = len(padre1) // 2
        hijo = padre1[:aux_operacion] + padre2[aux_operacion:]
        hijos.append(hijo)
    
    # Mutación
    for individuo in hijos:
        if mutate > random():
            prob_mut = randint(0, len(individuo)-1)
            if individuo[prob_mut] == 1:
                individuo[prob_mut] = 0
            else:
                individuo[prob_mut] = 1
    return hijos


def metodo_ruleta(best_aptos):

    def sortear(fitness_total, indice_a_ignorar=-1):            #El parámetro garantiza que no seleccionará el mismo elemento.
        ruleta, acumulado, valor_sorteado = [], 0, random()

        if indice_a_ignorar!=-1:                                #Reduce del total, la cantidad que se retirará del premio mayor
            fitness_total -= valores[0][indice_a_ignorar]

        for indice, i in enumerate(valores[0]):
            if indice_a_ignorar==indice:                        #ignora los valores que ya fueron usados en la ruleta.
                continue
            acumulado += i
            ruleta.append(acumulado/fitness_total)
            if ruleta[-1] >= valor_sorteado:
                return indice
    

    valores = list(zip(*best_aptos))                            #crea dos listas con valores de aptitud y cromosomas
    
    fitness_total = sum(valores[0])
    indice_padre_1 = sortear(fitness_total) 
    indice_padre_2 = sortear(fitness_total, indice_padre_1)

    padre_1 = valores[1][indice_padre_1]
    padre_2 = valores[1][indice_padre_2]
    
    return padre_1, padre_2


def readFile():
    raw_x = []
    with open('Alimentos.txt' , 'r') as f:
        for linea in f:
            lin = linea
            linea = lin.split()
            x = [float(x) for x in linea]
            raw_x.append(x)

        f.close()
        return raw_x 
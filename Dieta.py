from Calculos import *

                #[calorias , proteinas , grasas , carbohidratos]
alimentos = ['Aguacates' , 'Almendra' , 'Anguila' ,'Arandano' ,'Atun' ,'Avellana' ,'brie',
            'Caballa' ,'Cerdo' ,'Cheddar','Esparragos','Fresa','Huevo','Langosta','Leche entera',
            'Lechuga','Ostra','Parmesano','Pollo','res','Salmon','Sardinas','Yema de huevo','Mora',
            'Limon' ]

n_poblacion = 100                       #Tamaño de la población
generaciones = 50                       #Numero de generaciones (ciclos)


class Dieta():
    def __init__(self, TMB):
        self.TMB = TMB 

    def run_algorith(self):
        pesos_valores = readFile()
        n_cromosomas = len(pesos_valores)
        calorias_per_day = self.TMB                                                         #Total de calorias por día
        population = generate_population(n_poblacion , n_cromosomas)                        #Genera la población inicial
        print("Población:\n " , population)
        fitness_history = [media_fitness(population, calorias_per_day, pesos_valores)]      #Almacena el fitness obtenido

        for i in range(generaciones):
            population = selection(population, calorias_per_day, pesos_valores, n_poblacion)
            fitness_history.append(media_fitness(population, calorias_per_day, pesos_valores))
    
        #Impresiones en terminal 
        for indice , promd in enumerate(fitness_history):
            print ("Generación: ", indice ," | Promedio: ", promd)


        print("\nPeso máximo:", calorias_per_day ,"Kcalorias \nObjetos disponibles:")
        for indice , i in enumerate(pesos_valores):
            print("Alimento: ", indice+1,": ", "\t | kcalorias/100: ",i[0] ,"\t |Proteinas: " , i[1] , "\t |Grasas: " , i[2] , "\t |Carbo: " , i[3])
            

        print("\nPosibles soluciones: ")
        f = open ("Dieta.txt", "w")
        f.close()
        for i in range(5):
            print("Solución " , i+1)
            cont , cal , prot , gras , carb = 0 , 0 , 0 , 0 ,0
            print(population[i])
            f = open ("Dieta.txt", "a")
            f.write("----Opcion numero " + str(i+1) +"\n")
            for element in population[i]:
                if element == 1:
                    valor = pesos_valores[cont]
                    print("Alimento: " , alimentos[cont])
                    f.write("Alimento: " + str(alimentos[cont]) + "\n")

                    cal = cal + valor[0]            #Suma las calorias totales
                    prot = prot + valor[1]          #Suma las proteinas totales
                    gras = gras + valor[2]          #Suma las grasas totales
                    carb = carb + valor[3]          #Suma las carb totales

                cont += 1
            print("\nConsumo total: ")
            print("Calorias: " , cal)
            print("Proteinas: " , prot)
            print("Grasas: " , gras)
            print("carb: " , carb)
            print("------\n")
           
            f.write("\n\nConsumo total: \n")
            f.write("Calorias: " + str(cal) + "\n")
            f.write("Proteinas: " + str(prot) + "\n")
            f.write("Grasas: " + str(gras) + "\n")
            f.write("Carb: " + str(carb) + "\n")
            f.write("----------------------\n\n\n")
            f.close()


        #GERADOR DE GRAFICO
        from matplotlib import pyplot as plt
        plt.plot(range(len(fitness_history)), fitness_history)
        plt.grid(True, zorder=0)
        plt.title("Dieta Cétogenica")
        plt.xlabel("Generación")
        plt.ylabel("Calorias máximas")
        plt.show()

def main(TMB):
    print("Desde el main: " , TMB)
    model = Dieta(TMB)
    model.run_algorith()
    #readFile()
    
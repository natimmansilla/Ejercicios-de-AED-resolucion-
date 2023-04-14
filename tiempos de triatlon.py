__author__ = 'natimmansillagithub'
#titulo 
print("***"*50)
print("TIEMPOS DE TRIATLON")
print("***"*50)

##Caso de prueba:

#Carga de Datos
print("ingrese los siguientes tiempos en el formato minutos:segundos, es decir mm:ss")
print()\

time_natacion = input("Cargar tiempo de natación: ")
time_ciclismo = input("Cargar tiempo de ciclismo: ")
time_pedestre = input("Cargar tiempo pedestre: ")
#fin de carga de datos

#procesos
#creacion de tuplas con valor int
tupla_natacion = time_natacion
tupla_ciclismo = time_ciclismo
tupla_pedestre = time_pedestre

#llamado por indices a los valores de los minutos
mm_natacion = int(tupla_natacion[0] + tupla_natacion[1])
mm_ciclismo = int(tupla_ciclismo[0] + tupla_ciclismo[1])
mm_pedestre = int(tupla_pedestre[0] + tupla_pedestre[1])

#conversor de minutos a segundos
ss_natacion_total = mm_natacion*60 + int(tupla_natacion[3] + tupla_natacion[4])
ss_ciclismo_total = mm_ciclismo*60 + int(tupla_ciclismo[3] + tupla_ciclismo[4])
ss_pedestre_total = mm_pedestre*60 + int(tupla_pedestre[3] + tupla_pedestre[4])

#sumatoria de seguntos totales de las 3 diciplinas
ss_totales = ss_natacion_total + ss_ciclismo_total + ss_pedestre_total

#conversion de los segundos totales a horas( ya el dato definitivo de horas)
hh_finales,ss_restantes = divmod(ss_totales,3600)

#conversion de los segundos restantes a minutos (ya el dato definitivo de minutos)
mm_finales,ss_finales = divmod(ss_restantes,60)

#calculo de los tiempos maximos y minimos de las 3 disciplinas
time_max = max(ss_natacion_total,ss_ciclismo_total,ss_pedestre_total)
time_min = min(ss_natacion_total,ss_ciclismo_total,ss_pedestre_total)

#calculo del tiempo promedio de la prueba en segundos redondeados 2 decimales
time_promedio = round((ss_totales/3),2)

#fin de los procesos

#visualizacion de los resultados
print("el tiempo total de la prueba fue de: ",hh_finales,":",mm_finales,":",ss_finales)
print("el tiempo maximo fue de:",time_max,"segundos")
print("el tiempo minimo fue de:",time_min,"segundos")
print("el tiempo promedio fue de: ",time_promedio,"segundos")

#fin

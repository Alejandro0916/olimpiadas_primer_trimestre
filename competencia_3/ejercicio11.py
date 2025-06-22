print("****Ejercicio 11****")
print("------------------------------------------------------------------")
print("Ejercicio:Gestion de destinos turisticos") 
print("------------------------------------------------------------------")
#aqui creo las listas dadas para comenzar a codificar tomando como bases las 2 lsitas
viajeros = ["daniela","tomas","valeria"]
destinos = ["cartagena","madellin","san andres"]
#acontinuacion imprimo las listas para que el usuario pueda responder las siguientes preguntas
print("con las siguientes listas vas a responerlas siguientes preguntas")
print(f"lista viajeros es la siguiente: {viajeros}")
print(f"lista destinos es a siguiente: {destinos}")
print("------------------------------------------------------------------")
#aqui ya comienzo hacer las preguntas y comienzo a seguir los pasos que me dicen en el ejercicio 
condicion_1=input("valeria esta en las lista?: ")
condicion_mayus_1= condicion_1.upper()
#primera condicional
if condicion_mayus_1 == "SI" :
    viajeros.append("santiago")
    print(f"se a actualizado las lista viajeros la lista quedo de la siguiente forma: {viajeros}")
else:
    print("no se cumplen las condicionas para agregar a santiago")

#segunda condicionl
condicion_2 =input("san andres esta en la lista de destinos?: ")
condicion_mayus_2=condicion_2.upper()
if condicion_mayus_2 == "SI" :
    destinos.append("santa marta")
    print(f"se a actualizado las lista destinos la lista quedo de la siguiente forma:{destinos}")
else:
    print("no se cumplen con las condiciones para agregar a santa marta")
#tercera condicional 
condicion_3 = input("el la lista viajeros se encuentra tomas?: ")
condicional_mayus_3 =condicion_3.upper()
if condicional_mayus_3 == "SI":
    viajeros.remove("tomas")
    print(f"se a actualizado las lista viajeros la lista quedo de la siguiente forma: {viajeros}")
else: 
    print("no se cumplen con las condiones para poder eliminar a tomas")
#cuarta condicional
condicion_4 = input("hay mas de 3 elementos en la lista destinos?: ")
condicional_mayus_4 = condicion_4.upper()
if condicional_mayus_4 == "SI":
    destinos.pop(0)
    print(f"se a actualizado las lista destinos la lista quedo de la siguiente forma:{destinos}")
else:
        print("no se cumplen con las condiciones para eliminar a el primer valor de la lista destinos")
#quinta condicional
condicion_5 = input("en la lista viajeros esta daniela?: ")
condicional_mayus_5 = condicion_5.upper()
if condicional_mayus_5 =="SI":
     viajeros.remove("daniela")
     viajeros.append("julieta")
     print(f"se a actualizado las lista viajeros la lista quedo de la siguiente forma: {viajeros}")
else:
     print("no se cumple las condiciones para eliminar a daniela y agregar a julieta")
#aqui en el paso 6 y 7 me piden que cree una lista llamada "grupo 1" y que la cree con los primero 2 elementos de la lista viajeros y otra lista nueva que se llamen "costeños" con los dos ultimos elementos de la lista destinos
grupo_1=[viajeros[0],viajeros[-1]]
costeños=[destinos[-2],destinos[-1]]
print("se crearon 2 nuevas listas las listas son: ")
print(f"esta lista se llama grupo1 y es la siguiente:{grupo_1}")
print(f"ets lista se llama costeños y es la siguiente:{costeños}")
#octava condicional
condiciona_8=input("santa marta esta en las lista costeños?: ")
condicional_mayus_8 = condiciona_8.upper()
if condicional_mayus_8 =="SI":
     playa_destacada = ("santa marta", 4.7 )
     print(f"se creo una tupla la tupla es la siguiemte:{playa_destacada}")
else:
     print("las condiciones no se cumplen para crear la tupla playa_destacada")
#novena condicional
condicion_9 = input("julieta se encuentra en la lista grupo1?: ")
condicional_mayus_9 = condicion_9.upper()
if condicional_mayus_9 == "SI":
     grupo_1.append("check - in listo")
     print(f"la lista grupo1 ha sido actualizada quedo de la siguiente manera:{grupo_1}")
else:
     print("no se cumplen las condicones para que se puedan agregar check - in listo a la lista de grupo1")
#en el punto 10 nos dice que si check - in listo se encuentra en la lista grupo 1 hagamos un diccionario llamado reserva con las llaves: "nombre":"julieta","destino":"medellin","confirmado":True
condicion_10 = input("check - in listo se encuentra en la lista grupo1?: ")
condicional_mayus_10 = condicion_10.upper()
if condicional_mayus_10=="SI":
     reserva={
          "nombre":"julieta",
          "destino":"medellin",
          "confirmado":True
     }
     print(f"se creo el siguiemte diccionario llamado reserva este es el diccionario:{reserva}")
#onceava condicional 
condicion_11 = input("existe un diccionario llamado reserva?: ")
condicional_mayus_11 = condicion_11.upper()
if condicional_mayus_11 == "SI":
     reserva["vuelo"]="v-2345"
     print(f"se agregaron cosas al diccionario reserva el dicionario quedo de la siguiente forma:{reserva}")
else:
     print("no se cumplen las condiciones para  agregarle cosas al diccionario")
#doceaba condicion
condicion_12=input("bogota se encuentra en la lista destinos?:")
condicional_mayus_12= condicion_12.upper()
if condicional_mayus_12 =="NO":
     destinos.append("bogota")
     print(f"se agregaron cosas a las listas destinos la lista quedo de la siguiente manera: {destinos}")
else:
     print("no se cumplen las condiciones para agregar a bogota a la lista destinos")
#terceaba condicion
condicion_13 = input("tomas esta en la en la lista viajeros?: ")
condicional_mayus_13 =condicion_13.upper()
if condicional_mayus_13 =="NO":
     destinos.append("bogota")
     print(f"se agregaron cosas a las listas destinos la lista quedo de la siguiente maner: {destinos} ")
else : 
     print("no se cumplen las condiciones para poder agregar a bogota")
#ya por ultimo en el cuarteabo paso nos dice ya que imprimamos todo lo uqe viene siendo:listas,tuplas y diccionarios
print("------------------------------------------------------------------")
print("******LAS LISTAS,TUPLAS Y DICCIONARIOS QUEDARON DE LA SIGUIENTE FORMA:******")
print("------------------------------------------------------------------")
print(f"viajeros: {viajeros}")
print(f"destinos: {destinos}")
print(f"grupo1: {grupo_1}")
print(f"costeños: {costeños}")
print(f"el diccionario reserva:{reserva}")
print(f"la tupla playa destacada: {playa_destacada}")
print("------------------------------------------------------------------")

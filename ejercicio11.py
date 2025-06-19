print("ejercicio 11")

# aqui cumplo las primeras 5 condiciones que me dice que hagan
viajeros = ["daniela","tomas","valeria"]
destinos = ["cartagena","medellin","san andres"]
#paso 1
if "valeria" in viajeros :
    viajeros.append("santiago")
#paso 2 
if "san andres" in destinos :
    destinos.append("santa marta")
#paso 3
if "tomas" in viajeros :
    viajeros.remove("tomas")
#paso 4
if len(destinos) > 3 :
    destinos.pop(0)
#paso 5
if "daniela" in viajeros :
    viajeros.remove("daniela")
    viajeros.append("julieta")

# aqui cree las 2 listas que me soliciataron en el punto 6,7

grupo_1 = [viajeros[0],viajeros[1]]
costeños = [destinos[2]],destinos[-1]
#paso 8
if "santa marta" in costeños:
    playa_destacadas=("santa marta", 4.7)
#paso 9
if "julieta" in grupo_1 :
    grupo_1.append("check - in listo")
#paso 10
if "check - in listo" in grupo_1 :
    reserva = {
        "nombre" : "julieta",
        "destinos" : "medellin",
        "confirmados" : True
        }
#paso 11
if  reserva :
    reserva["vuelo"] = "v-2345"
#paso 12
if "bogota" not in destinos :
    destinos.append("bogota")
#paso 13
if "tomas" not in viajeros : 
    viajeros.append("tomas")
print(f"la lista viajeros quedo de la siguiente manera:{viajeros}")
print(f"la lista destinos quedo de la siguiente manera:{destinos}")
print(f"la lista grupo1 quedo de la siguiente manera:{grupo_1}")
print(f"la lista costeños quedo de la siguiente manera:{costeños}")
print(f"el diccionario quedo de la siguiente manera: {reserva}")
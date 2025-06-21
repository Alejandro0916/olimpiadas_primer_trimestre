print("****Ejercicio 4****")
print("Sistema de inversion")
total_invertir=int(input("ingrese el monto que quieres llegar con tu amigo:$"))
recolectado_amigo=int(input("ingrese el monto recolectado por tu amigo:$ "))
recolectado_por_ti=int(input("ingrese el monto recolectado por ti:$ "))
suma = recolectado_amigo + recolectado_por_ti
falta = suma - total_invertir
if suma > total_invertir : 
    print(f"felicidades haz superado el total a invertir, el moto recolectado fue de:${total_invertir}")
elif suma < total_invertir :
    print(f"no haz llegado al monto necesario su monto fue:${suma} te falta:${falta} para llegar a la meta")
elif suma == total_invertir :
    print(f"haz llegado justamente al total para invertir su monto recolectado fue:${suma}")
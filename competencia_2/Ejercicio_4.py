print("****Ejercicio 4 ****")
print("---------------------------------------------------------------------------")
print("Sistema de evaluacion")
print("---------------------------------------------------------------------------")
nom=input("ingrese su nombre: ")
n1 = float(input("agrege su primera nota: "))
n2 = float(input("agrege su segundo nota: "))
n3 = float(input("agrege su tercera nota: "))
prd = (n1 + n2 + n3)/3
if prd >= 3.0 :
    print(f"felicidades {nom} aprobastes con un promedio de:{prd}")
elif prd >=2.0 and prd <= 2.9 :
    print(f"{nom} haz habilitado con un promedio de: {prd}")
else: 
    print(f"perdistess {nom} con un promedio de:{prd}")    

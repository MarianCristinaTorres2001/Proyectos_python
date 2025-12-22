#PRIMER EJERCICIO
print("Programa que muestra el resultado de  multiplicar dos numeros si este es menor a 1000, sino los suma")
num1=int(input("Ingrese un numero entero: "))
num2=int(input("Ingrese otro numero entero: "))
resultado1=num1*num2
resultado2=num1+num2

if resultado1<=1000:
    print("El resultado de multiplicar ",num1," con ",num2, " es ",resultado1)
else: 
    print("El resultado de sumar ", num1, " con ",num2, " es ", resultado2)

#SEGUNDO EJERCICIO
valor_anterior=0
for i in range(1,10):
     print("El numero actual es: ",i," y el numero anterior es: ", valor_anterior, " entonces el resultado de sumarlos es: ",i+valor_anterior)
     valor_anterior+=1

#TERCER EJERCICIO 
print("Este programa solicita al usuario una palabra e imprime solo las letras de indice par")
palabra=(input("Ingrese una palabra: "))
print(palabra[0::2])

#forma alterna
palabra=(input("Ingrese una palabra: "))
tamano=len(palabra)

for i in range(0,tamano,2):
    print(palabra[i])

#CUARTO EJERCICIO
print("Este programa recorta la palabra en el indice indicado por el usuario")
indice_recorte=int(input("Ingrese el indice en el que desea recortar su palabra: "))

if indice_recorte>tamano: 
    print("Operacion no valida, el indice excede el numero de letras de la palabra.")
else:
    print(palabra[0:indice_recorte+1])

#QUINTO EJERCICIO
print("Este programa devuelve una palabra con las letras descartadas por el usuario")
print(palabra[indice_recorte+1:])

#SEXTO EJERCICIO
print("Este programa compara los elementos inicial y final de una lista, si son iguales devuelve true y si son diferentes devuelve false")
numbers_x=[10, 20, 30, 40, 10]
numbers_y=[75, 65, 35, 75, 30]


def Comparador(list):
    primer_elemento=list[0]
    ultimo_elemento=list[len(list)-1] 
    iguales=True

    if primer_elemento == ultimo_elemento:
        print(iguales)
    else:
        print(not iguales)

    
Comparador(numbers_x)
Comparador(numbers_y)


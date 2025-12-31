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

#SEPTIMO PROGRAMA
print("Este programa recibe una lista de numeros enteros y devuelve otra lista con solo los numeros divisibles entre 5")

numbers_z=[10, 20, 33, 46, 55]

def Divisores_Cinco(lista):
    for i in range (0,len(lista)):
        if lista[i]%5==0: 
            print(lista[i])

Divisores_Cinco(numbers_z)

#OCTAVO PROGRAMA
print("Este programa indica cuantas veces aparece cierta palabra en una cadena de caracteres en una cadena dada")
str_x="Emma is good developer. Emma is a writer. Emma is my best friend. Emma is a teacher"

def contador_palabras(string): 
     print(string.count("Emma"))

contador_palabras(str_x)  

#NOVENO PROGRAMA (aqui intento nuevamente lo anterior, pero sin usar el metodo count)
contador=0
for i in range(0,len(str_x)-3):
    if str_x[i:i+4]=="Emma":
        contador+=1

print("La palabra Emma aparece ",contador, " veces")


#DECIMO PROGRAMA
for i in range (6):
    for a in range (i):
         print(i, end=" ")
    print("\n")

#ONCEAVO PROGRAMA
print("Este programa indica si un numero es palindromo")

numeroA=11
numeroB=121
numeroC=125

def numero_palindromo(numero):
    texto=str(numero)
    textoinverso="".join(reversed(texto))
    if texto==textoinverso:
        print("El numero ",numero," es palindromo")
    else: 
        print("El numero ",numero," no es palindromo")

def palindromo_con_while(numero):
    numero_original=numero
    numero_invertido=0
    while numero>0:
        residuo=numero%10
        numero_invertido=(numero_invertido*10)+residuo
        numero=numero//10
    
    if numero_original==numero_invertido:
        print("El numero", numero_original, "es palindromo")
    else:
        print("El numero", numero_original, "no es palindromo")

    

numero_palindromo(11)
numero_palindromo(121)
numero_palindromo(125)
palindromo_con_while(11)
palindromo_con_while(121)
palindromo_con_while(125)


#DOCEAVO PROGRAMA
print("Programa que recibe dos listas y devuelve una nueva lista con los numeros impares de la primera y los pares de la segunda")

def lista(listaA,listaB):
    listaC=[]
    for valor in listaA:
        if valor%2==1:
            listaC.append(valor)

    for valor in listaB:
        if valor%2==0:
            listaC.append(valor)

    print("La lista resultante es ", listaC)

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
lista(list1,list2)

#PROGRAMA TRECE
print("Programa que escribe un numero en su orden inverso")

def inverso(numero):
    letras=str(numero)
    textoinverso="".join(reversed(letras))
    print("El numero ",numero, " al reves se lee como ",textoinverso)

def inverso2(numero):
    while numero>0:
            digito=numero%10
            numero=numero//10
            print(digito,end=", ")

inverso(7536)
inverso2(7536)

#PROGRAMA CATORCE
print("Programa que imprime las tablas de multiplicar del 1 al 10")
for i in range (1,11):
    for a in range (1,11):
        print(i*a, end=" ")
    print("\t")

#PROGRAMA QUINCE
print("Programa que imprime media priramide invertida") 

def piramide_invertida(numero):
    for i in range (numero+1):
        for a in range (i, numero+1):
            print("*", end=" ")
        print("\n")

piramide_invertida(6)

#PROGRAMA DIECISEIS
print("Programa que calcula la potencia de una cantidad")
def exponent(base, exp):
    resultado=base**exp
    print("El numero ", base, "elevado al expoente ", exp, "da como resultado", resultado)

exponent(2,5)
exponent(5,4)

#PROGRAMA DIESICIETE
print("Programa que genera los primeros quince terminos de la serie Fibonacci")
number1=0
number2=1
i=0
while i<15:
    resultado=number1+number2
    print(resultado, end=" ")
    number1=number2
    number2=resultado
    i=i+1

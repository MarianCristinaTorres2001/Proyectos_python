print("Hola mundo, este es mi primer programa en Python")
print("Estoy aprendiendo a programar en Python")
nombre="Marian"
#En este caso, se tiene que tener en cuenta la rebanada de caracteres termina en uno menos del valor indicado
# M=0, a=1, r=2, i=3, a=4, n=5 
print(nombre[1:4]) #aqui se imprime ari
#En este caso se imprrime desde el inicio hasta el indice 3 (4 no incluido)
print(nombre[:4])#aqui se imprime Mari
#En este caso se rescribe la cadena de caracteres completa
print(nombre[:]) #aqui se imprime Marian

#INDEXACION 
print(nombre[0]) #aqui se imprime M
print(nombre[1]) #aqui se imprime a
print(nombre[2]) #aqui se imprime r
print(nombre[3]) #aqui se imprime i
print(nombre[4]) #aqui se imprime a
print(nombre[5]) #aqui se imprime n

nombre1="teresa Chavez"
nombre1.capitalize()
print(nombre1.capitalize()) #Aqui se imprime Teresa chavez
nombre1.index("C")
print(nombre1.index("C")) #Aqui se imprime 7, que es la posicion de la letra C en la cadena de caracteres
nombre1.index("a")
print(nombre1.index("a")) #Aqui se imprime 5, que es la posicion de la letra a en la cadena de caracteres

numero=int(input("Escribe un numero: "))
print("El numero que escribiste es: ", numero)
print(type(numero))
estadocivil=bool(input("¿Eres soltero? (True/False):    "))
print("Cuando se pregunta si eres soltero, tu respuesta es: ", estadocivil)
print(type(estadocivil))

"El" + " " + "pais" + "mas pequeño del mundo es" + " " + "Vaticano"
print("El" + " " + "pais" + " mas pequeño del mundo es" + " " + "Vaticano")

print(20/4) #Aqui se imprime 5.0
print(20//4) #Aqui se imprime 5


x=5+3
y=10-2
print(x and y)

print((5<10) and (10>5)) #Aqui se imprime True
boleano1=(5<10) and (10>5)
print(boleano1) #Aqui se imprime True
print (not boleano1) #Aqui se imprime False


#Aqui presento unas sentencia condicional
velocidad=60
if velocidad>60:
    print("Estas excediendo el limite de velocidad")
else:
    print("Estas dentro del limite de velocidad")


ano_de_nacimiento=1990
if ano_de_nacimiento<2000:
    print("Tu año de nacimiento es: ",ano_de_nacimiento,"es hora de tener hijos y formar una familia ")
else:
    print("Aun eres joven para pensar en eso, ponte a ver television")

#Aqui presento una LISTA
paises=["Mexico","Colombia","Peru","Argentina","Chile"]
print(paises)
print(paises[0]) #Aqui se imprime Mexico
print(paises[2]) #Aqui se imprime Peru

#Aqui voy a agregar un pais al final de la  lista
paises.append("Venezuela")
print(paises)

#Aqui voy a agregar un pais en la posicion 2 de la lista
paises.insert(2,"Paraguay")
print(paises)

#Aqui voy a quitar un pais de la lista, en este caso Mexico
paises.remove("Mexico")
print(paises)

#Aqui voy a ver si Mexico esta en la lista
print("Mexico" in paises)

#Aqui voy a ver que indice tiene Paraguay en la lista
print(paises.index("Paraguay")) #aqui se imprime 1

#Aqui voy a actualizar el pais de Chile por Cuba
paises[4]="Cuba"
print(paises)

#Aqui voy contar cuantas veces aparece Paraguay en la lista
print(paises.count("Paraguay"))

#Aqui voy a ordenar la lista al reves
paises.reverse()
print(paises)

#TUPLAS
libros=("Crimen y castigo","Cien años de soledad","Don Quijote de la Mancha","La Iliada")
print(libros[0])

#DICCIONARIOS
calificaciones={"Matematicas":90, "Historia":85, "Ciencias":88}
print(calificaciones)
print(calificaciones["Matematicas"]) #Aqui se imprime 90
print(calificaciones["Historia"]) #Aqui se imprime 85

#Aqui voy a remover Historia del diccionario
del calificaciones["Historia"]
print(calificaciones)

#Aqui voy a revisar si Ciencias esta en el diccionario
print("Ciencias" in calificaciones) #Aqui se imprime True

#Aqui voy a cambiar Matematicas por Algebra
calificaciones["Algebra"]=calificaciones.pop("Matematicas")
print(calificaciones)

#Aqui voy a agregar una nueva materia al diccionario
calificaciones["Programacion"]=95
print(calificaciones)

commidas={
    "Desayuno": 200,
    "Comida": 600,
    "Cena": 400
    }

#Aqui voy a escribir mi primer ciclo For con python
for i in range(4):
    print("el numero asignado a esta iteracion es: ", i) #Aqui se imprimen los numeros 0,1,2,3


for i in range(1,4):
    print("el numero asignado a esta iteracion es: ", i) #Aqui se imprimen los numeros 1,2,3

for i in range(0,5,2):
    print("el numero asignado a esta iteracion es: ", i) #Aqui se imprimen los numeros 0,2,4

for char in "Marian":
    print(char)

for i in (1,2,3,4,5):
    print(i)

#Aqui voy a escribir mi primer ciclo While con python
x=10
    
while x<=18:
    print(x)
    x+=2

#Aqui voy a hacer algunas funciones

#en esta parte hago la defincion de funcion
def cubo(numerito):
    print("El cubo de ", numerito, " es: ", numerito**3)

def area_rectangulo(base, altura):
    area=base*altura
    print("El area del rectangulo con base ", base," con altura ", altura, " es ", area)

#en esta parte hago la llamada a la funcion
cubo(3)
area_rectangulo(5,10)

resultado=cubo(2)
print(resultado)

#Funciones recursivas
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

factorial(5)
print(factorial(5)) #Aqui se imprime 120

#Aqui trabajo con archivos de texto
#para abrir un archivo de trabajo
with open("razas_perros.txt", "r") as file:
     for linea in file:
            print("La raza de perro disponible para adoptar y su peso en kilogramos es: ", linea)

#para escribir un archivo de trabajo 
frase_cursi="Mi corazon no es de arena, pero tu estas dejando tu huella"
with open("cancion_bad_bunny.txt", "w") as file:
    file.write(frase_cursi)

#para agregar informacion a un archivo de trabajo
verso_siguiente= "\n \nY enséñame a bailar, mami, yo no sé \npero ya estoy borracho y son las tres \nYo quiero ver contigo el amanecer \nTu y yo solitos y el sol"

with open("cancion_bad_bunny.txt", "a") as file:
        file.write("\n \ncada vez que me miras \nsin parar de mover la cadera \nesto aqui no termina \nos fuimos rulin la noche entera")
        file.write(verso_siguiente)


#Aqui voy a probar las clausulas de excepecion usando try y except con division entre cero
num1=int(input("Ingrese un numero entero: "))
num2=int(input("Ingrese otro numero entero: "))

try: 
     resultado=num1/num2
     print("El resultado de la operacion es: ", resultado)
except: 
    print("Usted intento hacer una division entre cero o no ingreso un numero entero")


#Aqui voy a probar haciendo una excepcion especifica, para cuando se hace division entre cero. 
try: 
     resultado=num1/num2
     print("El resultado de la operacion es: ", resultado)
except ZeroDivisionError: 
    print("Usted intento hacer una division entre cero")
else:
    print("La division pudo realizarse con exito lo que significa que el dividendo no es cero")
finally:
    print("Gracias por usar el programa")

#Aqui voy a probar haciendo una excepcion a la que voy a nombrar como una variable. 
try: 
    resultado=num1/num2
    print("El resultado de la operacion es: ", resultado)
except ZeroDivisionError as e: 
    print(e)

#Aqui voy a probar las clausulas de excepcion de nuevo. Bueno aquí no funcionó. 
num3=int(input("Ingrese un numero mayor que 24: "))

try: 
    resultado1=num3
    resultado1>=24
    print("El numero ingresado es: ", resultado1 , " y es mayor o igual a 24")
except:
    print("El numero que usted ha ingresado no es mayor a 24")


#Aqui voy hacer una clase con su respectivos objetos o instancias. 
class ArchivoEscuela:
#estas son las instancias de la clase
    def __init__(self,nombre_alumno,grado,grupo,promedio_general):
        self.nombre_alumno=nombre_alumno
        self.grado=grado
        self.grupo=grupo
        self.promedio_general=promedio_general

#estos son los metodos de la clase
    def escribir_nombre(self):
        print(self.nombre_alumno)

    def escribir_grado(self):
        print(self.grado)
    
    def escribir_grupo(self):
        print(self.grupo)

    def escribir_promedio_general(self):
        print(self.promedio_general)

    def aumentar_promedio_general(self,puntos_extra):
        self.promedio_general+=puntos_extra
    
    def cambiar_grupo(self,grupo_nuevo):
        self.grupo=grupo_nuevo

#Aqui voy a crear las instancias de la clase
alumno1=ArchivoEscuela("Alejandro Rangel", "5","A", 9.4)
alumno2=ArchivoEscuela("Brenda Carolina", "3", "B", 8.0)

#Aqui voy a llamar a los metodos 
alumno1.escribir_nombre()
alumno1.escribir_grado()
alumno1.escribir_grupo()
alumno1.escribir_promedio_general()
alumno1.aumentar_promedio_general(0.6)
alumno1.escribir_promedio_general()
alumno1.cambiar_grupo("C")
alumno1.escribir_grupo()

alumno2.escribir_nombre()
alumno2.escribir_grado()
alumno2.escribir_grupo()
alumno2.escribir_promedio_general()
alumno2.aumentar_promedio_general(1)
alumno2.escribir_promedio_general()
alumno2.cambiar_grupo("F")
alumno2.escribir_grupo()


    


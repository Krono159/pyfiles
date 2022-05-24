from distutils.log import error
from inspect import Traceback
import traceback


suma = 1
resta = 2
multiplicacion = 3
division = 4
error = ""
try:
    print("Suma = 1")
    print("Resta = 2")
    print("Multiplicacion = 3")
    print("Division = 4")
    operacion = int(input("Que operacion desea realizar?"))
    num1 = int(input("Ingrese el primer numero:  \t"))
    print("primer numero: " +str(num1));
    num2 = int(input("Ingrese el segundo numero:  \t"))
    print("segundo numero: " +str(num2));
    if operacion == suma:
        try:
            resultado = num1 + num2
        except:
            error = "input error"
            raise
    elif operacion == resta:
        try:
            resultado = num1 - num2
        except:
            error = "input error"
            raise
    elif operacion == multiplicacion:
        try:
            resultado = num1 * num2
        except:
            error = "input error"
            raise
    elif operacion == division:
        try:
            resultado = num1 / num2
        except:
            error = "Math error, no se puede dividir por cero"
            raise
    else:
        error = "Operation error: no se ingreso una operacion valida"
    print("resultado: " + str(resultado))
except:
    if error == "":
        print("ha ingresado un argumento invalido, por favor vuelva a ejecutar el programa. error desconocido")
        print("Ahora, que carajos es mi existencia? solo soy 55 lineas de codigo...")
    else:
        print("ha ingresado un argumento invalido, por favor vuelva a ejecutar el programa. error: " + error )
        print("Ahora, que carajos es mi existencia? solo soy 55 lineas de codigo...")

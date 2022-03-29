print("hola")

#definimos una funcion
def mensaje():
    print("hola, que tl estas?")
    print("bien y tu?")
#y ahora llamamos a la funcion
mensaje()

#otro ejemplo, definiendo otra funcion
def suma():
    num1=5
    num2=12
    print(num1+num2)
#llamando a la funcion
suma()

#ahora una funcion declarando parametros o argumentos
def suma(a,b):
    print(a+b)
#llamamos a la funcion pero ahora hay que darle valores a los parametros
suma(5,3)   
suma(10,6)

#introducimos el concepto RETURN
def suma(a,b):
    resultado=a+b
    return resultado
#para poder ver el resultado que da return debemos usar print para poder verlo en el terminal
print(suma(4,5))
print(suma(7,8))


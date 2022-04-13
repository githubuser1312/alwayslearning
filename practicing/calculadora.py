from tkinter import *



root=Tk()
root.title("Calculadora Simple")
root.geometry("250x200")
root.resizable(0,0)

mainFrame=Frame(root,bd="1",bg="grey")
mainFrame.pack()

displayNumber=StringVar()
operacion=""
resultado=0

display=Entry(mainFrame, textvariable=displayNumber, bg="black",font="arial 16",fg="green", justify="right")
display.grid(row=0, column=0, columnspan=4,pady=4,padx=4)

def InsertaNumero(num):
    global operacion
    if operacion!="": #con este if indicamos que si es la primera vez que se pulsa la operacion...
        displayNumber.set(num)#....... se "resetee" el display y se introduzca un nuevo numero (no se siga concatenando numeros como en el "else")
        operacion=""  #con esta linea indicamos a la funcion que, despues del numero pulsado en la linea anterior, el valor de operacion es "" y por lo tanto puede ir al "else" para concatenar los números que se pulsen a continuacion.
    else:    
        displayNumber.set(display.get()+num)

def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion="suma"
    displayNumber.set(resultado)

#funcion elresutado para usar "="

def elresultado():
    global resultado
    displayNumber.set(resultado+int(displayNumber.get()))
    resultado=0
  
#otra forma de insertar números en el display
# def three():
#     display.insert(len(display.get()),3)

#la funcion lambda se pone para evitar que salga un numero en cuanto se abre la calculadora
Button(mainFrame, text="7", command=lambda:InsertaNumero("7"), height=2, width=4).grid(row=1,column=0, pady=2, padx=2)
Button(mainFrame, text="8", command=lambda:InsertaNumero("8"), height=2, width=4).grid(row=1,column=1, padx=1)
Button(mainFrame, text="9", command=lambda:InsertaNumero("9"), height=2, width=4).grid(row=1,column=2, padx=1)
Button(mainFrame, text="/", height=2, width=3).grid(row=1,column=3, padx=2)

Button(mainFrame, text="4", command=lambda:InsertaNumero("4"), height=2, width=4).grid(row=2,column=0, pady=2, padx=2)
Button(mainFrame, text="5", command=lambda:InsertaNumero("5"), height=2, width=4).grid(row=2,column=1, padx=1)
Button(mainFrame, text="6", command=lambda:InsertaNumero("6"), height=2, width=4).grid(row=2,column=2, padx=2)
Button(mainFrame, text="x", height=2, width=3).grid(row=2,column=3, padx=1)

Button(mainFrame, text="1", command=lambda:InsertaNumero("1"), height=2, width=4).grid(row=3,column=0, pady=2, padx=2)
Button(mainFrame, text="2", command=lambda:InsertaNumero("2"), height=2, width=4).grid(row=3,column=1, padx=1)
Button(mainFrame, text="3", command=lambda:InsertaNumero("3"), height=2, width=4).grid(row=3,column=2, padx=1)
Button(mainFrame, text="+", command=lambda:suma(displayNumber.get()), height=2, width=3).grid(row=3,column=3, padx=2)

Button(mainFrame, text="0", command=lambda:InsertaNumero("0"), height=2, width=4).grid(row=4,column=0, pady=2, padx=2)
Button(mainFrame, text=".", command=lambda:InsertaNumero("."), height=2, width=3).grid(row=4,column=1, padx=1)
Button(mainFrame, text="=", command=lambda:elresultado(), height=2, width=3).grid(row=4,column=2, padx=1)
Button(mainFrame, text="-", height=2, width=3).grid(row=4,column=3, padx=2)















root.mainloop()
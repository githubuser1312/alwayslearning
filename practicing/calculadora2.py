from tkinter import *

root=Tk()
root.title("CALCULADORA SIMPLE2")
root.resizable(1,1)
#main frame ________________________________________________
calculadoraFrame=Frame(root, width="300", height="300")
calculadoraFrame.pack()
#variables ________________________________________________
numberDisplay=StringVar()
operacion=""
#funciones ________________________________________________
def insertarNumero(num):
    global operacion
    if operacion!="": #para el caso en que se halla pulsado una tecla de operacion se "resetea" el display y se empieza a introducir un numero nuevo
        numberDisplay.set(num)
        operacion="" #una vez introducido el nuevo numero 
    else:
        numberDisplay.set(numberDisplay.get()+num)
def suma():
    global operacion
    operacion!=""
    numberDisplay.get()






#pantalla ________________________________________________
calculadoraDisplay=Entry(calculadoraFrame, textvariable=numberDisplay, bg="black", fg="green", justify="right")
calculadoraDisplay.grid(row=0,column=0,columnspan=4)
#botones numeros y coma ________________________________________________
Button(calculadoraFrame, command=lambda:insertarNumero("0"), bg="grey", text="0").grid(row=6,column=0, columnspan=2)
Button(calculadoraFrame, command=lambda:insertarNumero(","), bg="grey", text=",").grid(row=6,column=2)
Button(calculadoraFrame, command=lambda:insertarNumero("1"), bg="grey", text="1").grid(row=5,column=0)
Button(calculadoraFrame, command=lambda:insertarNumero("2"), bg="grey", text="2").grid(row=5,column=1)
Button(calculadoraFrame, command=lambda:insertarNumero("3"), bg="grey", text="3").grid(row=5,column=2)
Button(calculadoraFrame, command=lambda:insertarNumero("4"), bg="grey", text="4").grid(row=4,column=0)
Button(calculadoraFrame, command=lambda:insertarNumero("5"), bg="grey", text="5").grid(row=4,column=1)
Button(calculadoraFrame, command=lambda:insertarNumero("6"), bg="grey", text="6").grid(row=4,column=2)
Button(calculadoraFrame, command=lambda:insertarNumero("7"), bg="grey", text="7").grid(row=3,column=0)
Button(calculadoraFrame, command=lambda:insertarNumero("8"), bg="grey", text="8").grid(row=3,column=1)
Button(calculadoraFrame, command=lambda:insertarNumero("9"), bg="grey", text="9").grid(row=3,column=2)
#botones operaciones ___________________________________________________
Button(calculadoraFrame, bg="grey", text="=").grid(row=6,column=3)
Button(calculadoraFrame, bg="grey", text="x").grid(row=5,column=3)
Button(calculadoraFrame, bg="grey", text="-").grid(row=4,column=3)
Button(calculadoraFrame, command=suma(), bg="grey", text="+").grid(row=3,column=3)
Button(calculadoraFrame, bg="grey", text="AC").grid(row=2,column=0)
Button(calculadoraFrame, bg="grey", text="+/-").grid(row=2,column=1)
Button(calculadoraFrame, bg="grey", text="%").grid(row=2,column=2)
Button(calculadoraFrame, bg="grey", text="/").grid(row=2,column=3)







root.mainloop()
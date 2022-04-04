# GUI interface grafica con libreria Tkinter

# Tkinter es un puente entre la linreria TCL/TK y Python

#Estructura: RAIZ(tk)o ventana (que es un widget), dentro esta FRAME(que es un widget) y dentro los WIDGETS

#consultar docs.pyton.org/librarytk

from tkinter import *

root=Tk()

root.title("Ventana de pruebas") 

root.resizable(1,1) #método para cambiar tamaño o no de ventana, es booleano y se puede indicar True/False o con 1/0 !!!!NO FUNCIONA BIEN¿¿¿¿PORQUE??????_____________

#raiz.geometry("650x350") #se lo quito cuando le daoy tamaño al frame

root.iconbitmap("learningpython/pictures/icono1.ico") #NO FUNCIONA !!!!!!!!!!___________
root.config(bg="blue")


#FRAMES
myFrame=Frame(root, width="650",height="350")#debemos meter el Frame dentro de la raiz (empaquetarlo)
myFrame.pack(fill="x")#asi empaquetamos el frame
myFrame.config(bg="grey",)
myFrame.config()#para dar el tamño al Frame hay que quitarle el tamaño al Frame
myFrame.config(relief="groove")
myFrame.config(bd=35)
myFrame.config(cursor="pirate")


#LABELS
# myLabel=Label(myFrame, text="Hello guys")
# myLabel.place(x=100, y=200) 
#se puede simplificar el codigo de las dos lineas de arriba de la siguiente manera (solo en caso de que no usemos mas la variable myLabel):
Label(myFrame, text="Hello guys", font="18", fg="blue", bg="yellow").place(x=100, y=200)
myImage=PhotoImage(file="learningpython/pictures/image01.png")
myLabel2=Label(myFrame, image=myImage)
myLabel2.place(x=200,y=50)










root.mainloop() #este método lo que hace es un "bucle infinito" para que la ventana este siempre a la escuche de "eventos". ¡¡¡¡ SIEMPRE TIENE QUE ESTAR AL FINAL DEL CODIGO!!!!!!!!



# GUI interface grafica con libreria Tkinter

# Tkinter es un puente entre la linreria TCL/TK y Python

#Estructura: RAIZ(tk)o ventana (que es un widget), dentro esta FRAME(que es un widget) y dentro los WIDGETS

#consultar docs.pyton.org/librarytk

from tkinter import *

from click import command

root=Tk()

root.title("Ventana de pruebas") 

root.resizable(1,1) #método para cambiar tamaño o no de ventana, es booleano y se puede indicar True/False o con 1/0 !!!!NO FUNCIONA BIEN¿¿¿¿PORQUE??????_____________

#raiz.geometry("650x350") #se lo quito cuando le daoy tamaño al frame

root.iconbitmap("learningpython/pictures/icono1.ico") #NO FUNCIONA !!!!!!!!!!___________
root.config(bg="blue")


#FRAMES
myFrame=Frame(root, width="650",height="350")#debemos meter el Frame dentro de la raiz (empaquetarlo)
myFrame.pack(fill="x")#asi empaquetamos el frame y sirve para que "root" se haga tan grande como lo necesiten los elementos que contiene.
myFrame.config(bg="grey")
myFrame.config(relief="groove")
myFrame.config(bd=5)
myFrame.config(cursor="pirate")


#LABELS
# myLabel=Label(myFrame, text="Hello guys")
# myLabel.place(x=100, y=200) 

#se puede simplificar el codigo de las dos lineas de arriba de la siguiente manera (solo en caso de que no usemos mas la variable myLabel):
Label(myFrame, text="Nombre: ", font="18", fg="blue", bg="white").grid(row=0,column=0, sticky="e",padx=3,pady=10)#DENTRO DE FRAME, SI USAMOS GRID NO PODEMOS USAR PLACE, sticky es la ubicacion dentro del label
Label(myFrame, text="Apellido: ", font="18", fg="blue", bg="white").grid(row=1,column=0, sticky="e", padx=3,pady=10) 
Label(myFrame, text="Direccion: ", font="18", fg="blue", bg="white").grid(row=2,column=0, sticky="e", padx=3,pady=10)
Label(myFrame, text="Password: ", font="18", fg="blue", bg="white").grid(row=3,column=0, sticky="e", padx=3,pady=10)
Label(myFrame, text="Comentarios: ", font="18", fg="blue", bg="white").grid(row=4,column=0, sticky="e", padx=3,pady=10)

myImage=PhotoImage(file="learningpython/pictures/image01.png")
myLabel2=Label(root, image=myImage)
myLabel2.place(x=0,y=560) #AQUI PODEMOS USAR PLACE PORQUE NO USAMOS GRID en root



#ENTRY
miNombre=StringVar()#esta linea se añade para mostrar como funciona el Button de más abajo

nameframe=Entry(myFrame, textvariable=miNombre)#textvariable es para linkar la variaboe miNombre a este cuadro de texto.
nameframe.grid(row=0,column=1)
nameframe.config(fg="red", justify="center")
apellidoframe=Entry(myFrame)
apellidoframe.grid(row=1,column=1)
direccionframe=Entry(myFrame)
direccionframe.grid(row=2,column=1)
passwordframe=Entry(myFrame)
passwordframe.grid(row=3,column=1)
passwordframe.config(show="*")


#TEXT
textComentario=Text(myFrame, width=26, height=10)
textComentario.grid(row=4,column=1)
scrollVert=Scrollbar(myFrame, command=textComentario.yview)
scrollVert.grid(row=4,column=2, sticky="nsew") #sticky es para posicionarlo del mismo tamaño que el cuador de texto
textComentario.config(yscrollcommand=scrollVert.set)#posiciona la barra movible del scroll a la altura del texto que estamos escribiendo o editando


#BUTTON
def codigoBoton():
    miNombre.set("Juan")#con set asignamos un valor a la variable miNombre que hemos definido en la zona de ENTRY justo encima del ENTRY de nameframe

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()


#PRACTICA DE CALCULADORA (ver en carpeta practicing)



#RADIOBUTTON

varOpcion=IntVar()

def imprimir():
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido Masculino")
    else:
        etiqueta.config(text="Has elegido Femenino")

Label(root, text="Genero: ").pack()
Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
etiqueta=Label(root)
etiqueta.pack()



#CHECKBUTTON 
#A diferencia de Radiobutton, este nos deja elegir varias opciones al mismo tiempo

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionViaje():
    opcionEscogida=""
    if playa.get()==1:
        opcionEscogida+=" playa"
    if montana.get()==1:
        opcionEscogida+=" montaña"
    if turismoRural.get()==1:
        opcionEscogida+=" turismo rural"
    textoFinal.config(text=opcionEscogida)



imagen=PhotoImage(file="learningpython/pictures/flores.png")
Label(root, image=imagen).pack()
frame=Frame(root)
frame.pack()
Label(frame, text="Elije destinos", width=50).pack()
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop() #este método lo que hace es un "bucle infinito" para que la ventana este siempre a la escuche de "eventos". ¡¡¡¡ SIEMPRE TIENE QUE ESTAR AL FINAL DEL CODIGO!!!!!!!!



# GUI interface grafica con libreria Tkinter

# Tkinter es un puente entre la linreria TCL/TK y Python

#Estructura: RAIZ(tk)o ventana (que es un widget), dentro esta FRAME(que es un widget) y dentro los WIDGETS

#consultar docs.pyton.org/librarytk

from cProfile import label
from email.errors import NoBoundaryInMultipartDefect
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

nameframe=Entry(myFrame, textvariable=miNombre)#textvariable es para linkar la variable miNombre a este cuadro de texto.
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
#los cuadros de texto no tienen "textvariable" asi que no se le puede adjudicar una variable al valor que alojan del tipo StringVar o similar. Ver el ejemplo de bbdd.py creado para ver como se resuelven algunos temas con este tipo de cuadro
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

#MENU

#!!!!!!!IMPORTANTE¡¡¡¡¡¡¡¡----EL MENU NO APARECE EN ROOT APARECE EN LA PARTE SUPERIOR EN MAC (EN WINDOWS SI APARECE DENTRO DE ROOT)
barraMenu=Menu(root)
root.config(menu=barraMenu) #lo asignamos a la base

archivoMenu=Menu(barraMenu, tearoff=0) #tearoff es para quitar una linea discontinua que aparece en windows (no en Mac)
archivoMenu.add_command(label="Nuevo")#elemento del menu desplegable
archivoMenu.add_command(label="Guardar")#elemento del menu desplegable
archivoMenu.add_command(label="Guardar como")#elemento del menu desplegable
archivoMenu.add_separator() #añade una linea de separacion dentro del menu desplegable



archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)#el submenu se vera en el siguiente apartado de VENTANA EMERGENTE


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



#VENTANA EMERGENTE
from tkinter import messagebox

def infoAdicional():
    messagebox.showinfo("Procesador JAP", "Procesador de textos 2018")#showinfo gestina el símbolo que aparece en el cuadro del mensaje
def avisoLicencia():
    messagebox.showwarning("licencia", "producto bajo licencia GNU") #"licencia" es el titulo de la ventana pero no aparece en mac (si en windows), Showwarning cambia el símbolo que utiliza el cuadro de mensaje
def salirAplicacion():
    #valor=messagebox.askokcancel("salir", "Deseas salir de la aplicación?")#este messagebox devuelve un valor "true" o "false"
    valor=messagebox.askquestion("salir", "Deseas salir de la aplicación?")#este messagebox devuelve un valor "yes" o un valor "no" que se puede almacenar en una variable, ene ste caso la llamo "valor", para luego usarla y hacer algo.
    if valor=="yes":
        root.destroy() #para salir de la aplicacion
def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado")
    if valor==False:
        root.destroy()
archivoAyuda.add_command(label="Acerca de", command=infoAdicional) 
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)

archivoMenu.add_command(label="Salir", command=salirAplicacion)#elemento del menu desplegable anterior que pongo aqui para usarla como ejemplo de messagebox
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)#elemento del menu desplegable


from tkinter import filedialog

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel","*.xlsx"),("Ficheros de texto","*.txt"))) #IMPORTANTE¡¡¡¡¡¡¡¡: EN LA TUPLA HAY QUE PONER AL MENOS DOS TIPOS DE ARCHIVOS¡¡¡¡¡¡¡¡¡
    print(fichero)
Button(root, text="Abrir Fichero", command=abreFichero).pack()



root.mainloop() #este método lo que hace es un "bucle infinito" para que la ventana este siempre a la escuche de "eventos". ¡¡¡¡ SIEMPRE TIENE QUE ESTAR AL FINAL DEL CODIGO!!!!!!!!



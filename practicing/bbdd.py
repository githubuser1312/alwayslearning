from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()
root.title("BBDD de Personal")
root.resizable(0,0)
root.geometry("+200+100")#posiciona en el monitor, no pongo las dimensiones principales porque se definen mas abajo


#una vez creada la BBDD, la comento para que no se intente crear de nuevo cada vez que ejecuto el codigo
def creaBBDD():
    miConexion=sqlite3.connect("ListaPersonal")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE PERSONAL (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(20),
                PASSWORD VARCHAR(20),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(100),
                COMENTARIOS VARCHAR(250)
                )
            ''')
        miCursor.execute("INSERT INTO PERSONAL VALUES (NULL, 'JOSE','333','PEREZ', 'CALLE X', 'VARIOS COMENTARIOS')")
        miCursor.execute("INSERT INTO PERSONAL VALUES (NULL, 'Luis','444','Gomez', 'CALLE Y', 'VARIOS COMENTARIOS')")
        messagebox.showinfo("Información","La BBDD ha sido creada con éxito")
    except sqlite3.OperationalError:
        messagebox.showwarning("Error", "La base de datos ya fue creada anteriormente")
    miConexion.commit()
    miConexion.close()

#TOdo, VER COMO CAMBIAR YES A SI
def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor=="yes": 
        root.destroy()

ID=StringVar()
Nombre=StringVar()
Apellido=StringVar()
Password=StringVar()
Direccion=StringVar()
# Comentarios=StringVar()  este no se define porque el campo Text no tiene textvariable

def borrarCampos():
    valor=messagebox.askquestion("Atención", "¿Está seguro desea borrar toda la información?")
    if valor=="yes":
        ID.set("")
        Nombre.set("")
        Password.set("")
        Apellido.set("")
        Direccion.set("")
        textComentarios.delete(1.0, END) #para borrar todo lo insertado en el cuadro Text, se usa la propiedad "delete" directamente sobre el cuadro de texto creado añadiendo desde donde hasta donde se borrará

def crearPersona():
    miConexion=sqlite3.connect("ListaPersonal")
    miCursor=miConexion.cursor()
    # miCursor.execute("SELECT id FROM PERSONAL WHERE id=(SELECT max(ID) FROM PERSONAL)")
    # ultimoID=miCursor.fetchone()
    # ID.set(ultimoID[0]+1)
    #entryId.config(state="disable")#no tiene sentido esta linea, pero lo dejo para saber como se deshabilita 
    # miCursor.execute("INSERT INTO PERSONAL VALUES (NULL,'" + Nombre.get() + "' ,'" + Password.get() + "' ,'" + Apellido.get() + "' ,'" + Direccion.get() + "' ,'" + textComentarios.get("1.0" , END) + "' )")#get se usa directamente sobre el cuadro de texto (no se puede crear una variable que aluda al cuadro de texto porque no existe textvariable para los cuadros de texto)
    #OTRA FORMA de hacer lo de la linea anterior, que es mucho mas correcto, es haciendo una consulta PARAMETRIZADA. A continuacion se explica:
    datos=(Nombre.get(),Password.get(),Apellido.get() ,Direccion.get(),textComentarios.get("1.0" , END))
    miCursor.execute("INSERT INTO PERSONAL VALUES (NULL,?,?,?,?,?)", datos)
    miConexion.commit()
    messagebox.showinfo("BBDD", "Se ha guardado con exito el nuevo registro")

def leerPersona():
    miConexion=sqlite3.connect("ListaPersonal")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM PERSONAL WHERE ID=" + ID.get())
    persona=miCursor.fetchone()
    Nombre.set(persona[1])
    Password.set(persona[2])
    Apellido.set(persona[3])
    Direccion.set(persona[4])
    textComentarios.insert(1.0, persona[5])
    miConexion.commit()
  

def updatePersona():
    miConexion=sqlite3.connect("ListaPersonal")
    miCursor=miConexion.cursor()
    # miCursor.execute("SELECT id FROM PERSONAL WHERE id=(SELECT max(ID) FROM PERSONAL)")
    # ultimoID=miCursor.fetchone()
    # ID.set(ultimoID[0]+1)
    # miCursor.execute("UPDATE PERSONAL SET NOMBRE='" + Nombre.get() + "' , PASSWORD = '" + Password.get() + "', APELLIDO='" + Apellido.get() + "', DIRECCION= '" + Direccion.get() + "', COMENTARIOS= '" + textComentarios.get(1.0, END) + "' WHERE ID = " + ID.get())#get se usa directamente sobre el cuadro de texto (no se puede crear una variable que aluda al cuadro de texto porque no existe textvariable para los cuadros de texto)
    #OTRA FORMA de hacer lo de la linea anterior, que es mucho mas correcto, es haciendo una consulta PARAMETRIZADA. A continuacion se explica:
    datos=(Nombre.get(),Password.get(),Apellido.get() ,Direccion.get(),textComentarios.get("1.0" , END))
    miCursor.execute("UPDATE PERSONAL SET NOMBRE=? , PASSWORD = ?, APELLIDO=?, DIRECCION= ?, COMENTARIOS= ? WHERE ID = " + ID.get(), datos)
    miConexion.commit()
    messagebox.showinfo("BBDD", "Se ha actualizado con exito el registro")
   

def deletePersona():
    miConexion=sqlite3.connect("ListaPersonal")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM PERSONAL WHERE ID=" + ID.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con exito")


#barra menu______________________________________________
barraMenu=Menu(root)
root.config(menu=barraMenu) #hay que indicar al root que tiene un menu que se llama barraMenu
menuBBDD=Menu(barraMenu, tearoff=0) #dentro de la barraMenu creamos un nuevo menu que se llama menuBBDD
menuBBDD.add_command(label="Conectar",command=creaBBDD) #dentro del nuevo menu creamos etiquetas que llevaran un comando asociado
menuBBDD.add_command(label="Salir", command=salirAplicacion)
menuBorrar=Menu(barraMenu,tearoff=0)#otro menu dentro de barraMenu
menuBorrar.add_command(label="Borrar campos", command=borrarCampos)
menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label="Create", command=crearPersona)
menuCRUD.add_command(label="Read", command=leerPersona)
menuCRUD.add_command(label="Update", command=updatePersona)
menuCRUD.add_command(label="Delete", command=deletePersona)
menuAyuda=Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Licencia")
menuAyuda.add_command(label="Acerca de")
barraMenu.add_cascade(label="BBDD", menu=menuBBDD) 
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="CRUD", menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
#etiquetas y sus entry o text _______________________________
labelId=Label(root, text="I.D.", width=18)
labelId.grid(row=0, column=0, columnspan=2)
entryId=Entry(root, width=18, textvariable=ID)
entryId.grid(row=0, column=2, columnspan=2)

labelNombre=Label(root, text="Nombre", width=18)
labelNombre.grid(row=1, column=0, columnspan=2)
entryNombre=Entry(root, width=18, fg="red", justify="right", textvariable=Nombre)
entryNombre.focus_set()#establezco el foco en este entry por defecto
entryNombre.grid(row=1, column=2, columnspan=2)

labelPassword=Label(root, text="Password", width=18)
labelPassword.grid(row=2, column=0, columnspan=2)
entryPassword=Entry(root, width=18, show="*", textvariable=Password)
entryPassword.grid(row=2, column=2, columnspan=2)

labelApellido=Label(root, text="Apellido", width=18)
labelApellido.grid(row=3, column=0, columnspan=2)
entryApellido=Entry(root, width=18, textvariable=Apellido)
entryApellido.grid(row=3, column=2, columnspan=2)

labelDireccion=Label(root, text="Dirección", width=18)
labelDireccion.grid(row=4, column=0, columnspan=2)
entryDireccion=Entry(root, width=18, textvariable=Direccion)
entryDireccion.grid(row=4, column=2, columnspan=2)

labelComentarios=Label(root, text="Comentarios", width=18)
labelComentarios.grid(row=5, column=0, columnspan=2)
textComentarios=Text(root, height=10, width=22, borderwidth=1, relief="groove") #text no admite textvariable
textComentarios.grid(row=5, column=2, columnspan=2)
scrollVert=Scrollbar(root, command=textComentarios.yview, width=8)
scrollVert.grid(row=5,column=4, sticky="nsew") #sticky es para posicionarlo del mismo tamaño que el cuadro de texto
textComentarios.config(yscrollcommand=scrollVert.set)#posiciona la barra movible del scroll a la altura del texto que estamos escribiendo o editando

#botones____________________________________________________________________________
buttonCreate=Button(root, text="Create", width=8, command=crearPersona)
buttonCreate.grid(row=6, column=0)
buttonRead=Button(root, text="Read", width=8, command=leerPersona)
buttonRead.grid(row=6, column=1)
buttonUpdate=Button(root, text="Update", width=8, command=updatePersona)
buttonUpdate.grid(row=6, column=2)
buttonDelete=Button(root, text="Delete", width=8, command=deletePersona)
buttonDelete.grid(row=6, column=3)


root.mainloop()


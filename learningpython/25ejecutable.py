#primero instalar pyinstaller
#en la terminal vamos a donde esta la aplicacion 
# en terminal escribir (en el directorio donde este ubicado el archivo):
#           $ pyinstaller  nombre_archivo.py
#esto generara muchos archivos entre los que se encuentra (en la carpeta dist) el 
# ejecutable. Además, al ejecutar el archivo se ejecuta también la terminal 
# (al menos en windows). Para que NO SALG ALA TERMINAL:
#           $ pyinstaller  --windowed nombre_archivo.py
#Para que todo el programa se compile en UN SOLO ARCHIVO (sin los archivos y carpetas adjuntas)
#           $ pyinstaller  --windowed --onefile nombre_archivo.py
#Para aregar un icono al programa autoejecutable que se genera con pyinstaller, tenemos que guardar un archivo .ico al lado del archivo original nombre_archivo.py  y además:
#      $ pyinstaller  --windowed --onefile --icon=./nombre_icono.ico nombre_archivo.py

#./ es en este caso, el mismo directorio donde se esta ejecuntando pyinstaller que es donde se encuentran tanto "nombre_icono.ico"  como  "nombre_archivo.py"
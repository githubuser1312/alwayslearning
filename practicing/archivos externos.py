from io import open

archivo_temporal=open("practicing/archivo_permanente","wt")
texto_a_incluir="esto es una prueba de practica"
archivo_temporal.write(texto_a_incluir)
archivo_temporal.close()
archivo_temporal_para_lectura=open("practicing/archivo_permanente","rt")
texto_leido=archivo_temporal_para_lectura.read()
print(texto_leido)



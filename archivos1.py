from io import open

archivo_texto=open('pruebaaaa.txt', 'a')
archivo_texto.write(archivo_texto.write(f"\nred: trojo"))
archivo_texto.close() 
#print(archivo_texto.readlines())
""" print(archivo_texto.read())
archivo_texto.seek(0)
print(archivo_texto.read()) """

""" for lineas in archivo_texto.readlines():
    print(lineas.rsplit())
    print(lineas)
archivo_texto.close()
 """

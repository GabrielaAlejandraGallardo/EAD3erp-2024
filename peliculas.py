#peliculas variable que guarda el diicionario
           #clave para la primer pelicula
            #|        #a PO1 LE ASIGNAMOS COMO VALOR OTRO DICCIONARIO                            clave 2 diccionario contenido en el diccionario peliculas
peliculas={"P01":{"Nombre":"Rey León","Estreno":2002,"Protagonista":"Simba","Género":"Animada"},
           "P02":{"Nombre":"La Escaloneta","Estreno":20234,"Protagonistas":("Scaloni","Messi","Di Maria","Martines x2","Fernandes","Paredes"),"Género":"Documental"}}
                  #clave1   #valor 1    clave2  valor2 clave3        valor3  clave4  valor4             clave1   #valor 1         clave2  valor2 clave3        valor3                                                                  clave4  valor4   
print(peliculas)
print("_________________________________________________________________________")
      #c de clave, v de valor de la clave  
for c,v in peliculas.items():
    print(c, ":",v )
    print("_________________________________________________________________________")
        
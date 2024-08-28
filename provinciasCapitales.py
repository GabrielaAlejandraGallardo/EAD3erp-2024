#Crear un programa que guarde en un diccionario las provincias argentinas 
# con sus respectivas capitales,luego las muestre
provincias={"Córdoba":"Córdoba","Buenos Aires":"La Plata", }


pciaBuscarValorCapital=input("Ingresar provincia a buscar capital: ")
#Buscamos el valor por clave, en este caso capital ingresando provincia
x = provincias[pciaBuscarValorCapital]
print("su capital es:",x)
print("_______________________")
#Agregamos elemento al diccionario
pciaAgregar=input("Ingrese la provincia que desea agregar:")
capitalpcia=input("Ingrese la capital de la provincia agregada:")
provincias[pciaAgregar]=capitalpcia
print("_______________________")
for p, c in provincias.items():
    print(p, "-", c)
            
            
            
            
            
            
            
            
            
            
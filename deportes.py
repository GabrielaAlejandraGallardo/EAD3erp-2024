deportes={"D1":"Futbol", "D2":"Voley", "D3":"Tennis"}

for c,v in deportes.items():
    print(c, ":", v)
    print(f"{c} : {v}")
    if "Voley" in v:
        print("El deporte Voley existe y tiene clave:", c)
          
# INICIO DE SOFTWARE

|FUNCIONES|QUE HACE|
|--|:--|
|COORDINACION|tiene la funcion de visualizar a os trainers y aceptar campers a un nuevo progreso|
|TRAINER| Tiene la funcion de asignar notas y dar puntos positivos a los campers|
|REGISTRO|Permite que aquellos que quieran ingresar a las instalaciones puedan registrarse para posterior ser aceptados por el coordinador|
|CAMPER| Tiene la funcion de poder ver sus notas Ver su estado ver cuantos puntos positivos o negativos se tienen |

> [!IMPORTANT]  
> La funcion de Trainer NO decide si el camper pasa o no, Solo puede asignar notas y puntos

> [!IMPORTANT]  
>Solo puede ver sus notas NO puede MODIFICAR NADA


```python
def ver():
    with open("todos.json") as file:
        nte = json.load(file)
    rr = ["1.para ver notas", "2.para ver estado","3.para ver el riesgo","4.para retroceder"]
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("ingresa tu salon")
        print("U1  U2  U3  U4")
        try:
            car = input("->")
            for i in nte[car]:
                print(i)
            break
        except Exception:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("no existe- recuerda que la primera letra es en mayuscula")
                print("el numero tiene que estar en el rango del curso")
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("escriba su documento a modificar(recuerde que tiene qe estar en los documentos anteriores)")
        try:
            doc = input("->")
            print("perfecto, ingresa --",nte[car][doc]["nombres"])
            break
        except Exception:
            print("documento no valido")```

def nota():
    yy = ["1 para cambiar la nota del 60%","2. para cambiar la nota del 30%","3. para cambiar la nota del 10%"]
    with open("todos.json") as file:
        nte = json.load(file)
    print("seleccione uno de los cursos")
    print("U1","U2","U3","U4")
    while True:
        try:
            car = input("....")
            for i in nte[car]:
                print(i)
            break
        except Exception:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("no existe- recuerda que la primera letra es en mayuscula")
            print("el numero tiene que estar en el rango del curso")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
   # print("escriba su documento a modificar(recuerde que tiene que estar en los documentos anteriores)")
    while True:
        print("escriba su documento a modificar(recuerde que tiene que estar en los documentos anteriores)")
        try:
            doc = input("->")
            print("La del 60% es", nte[car][doc]["notas 60"], " del 30% ",nte[car][doc]["notas 30"]," y del 10% es", nte[car][doc]["notas 10"])
            break
        except Exception:
            print("documento no valido")
    print("deseas elegir")
    for i in yy:
        print(i)
    while True:
        gg = int(input("->"))
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        if gg == 1:
            nte[car][doc]["notas 60"] = int(input("ingrese la nueva nota->"))
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        elif gg == 2:
            nte[car][doc]["notas 30"] = int(input("ingrese la nueva nota->"))
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        elif gg == 3:
            nte[car][doc]["notas 10"] = int(input("ingrese la nueva nota->"))
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        else:
            print("no existe")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            break
        resultadoT = (nte[car][doc]["notas 60"]*0.6) + (nte[car][doc]["notas 30"]*0.3)+(nte[car][doc]["notas 10"]*0.1)
        if resultadoT < 100:
            nte[car][doc]["riesgo"] = "bajo"
        elif resultadoT < 60:
            nte[car][doc]["riesgo"] = "medio"
        elif resultadoT < 30:
            nte[car][doc]["riesgo"] = "alto"
        elif resultadoT < 10:
            nte[car][doc]["riesgo"] = "papa ya filtrado"
        nte[car][doc]["nota final"] = resultadoT
        contenido = json.dumps(nte ,indent=4)
        with open("todos.json","w") as file:
            file.write(contenido)
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        n = input("deseas continuar marca si, si no marca enter")
        if n == "":
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("saliendo...")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            break


        contenido = json.dumps(nte ,indent=4)
        with open("todos.json","w") as file:
            file.write(contenido)```




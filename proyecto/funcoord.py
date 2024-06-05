import json

def mod_esta():
    with open("todos.json") as file:
        nte = json.load(file)
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("seleccione uno de los cursos")
        print("U1","U2","U3","U4")
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
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
    
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("escriba su documento a modificar(recuerde que tiene qe estar en los documentos anteriores)")
        try:
            doc = input("->")
            print("el estado del estudiante",nte[car][doc]["nombres"]," es",nte[car][doc]["estado"])
            break
        except Exception:
            print("documento no valido")
    print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
    ff= input("ingrese el estado a colocar al estudiante")
    nte[car][doc]["estado"] = ff
    contenido = json.dumps(nte, indent=4)  
    with open("todos.json","w") as file:
            file.write(contenido)

def mod_ries():
    with open("todos.json") as file:
        nte = json.load(file)
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("seleccione uno de los cursos")
        print("U1","U2","U3","U4")
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
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
    
    print("escriba su documento a modificar(recuerde que tiene qe estar en los documentos anteriores)")
    while True:
        try:
            doc = input("->")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("el riesgo del estudiante",nte[car][doc]["nombres"]," es",nte[car][doc]["riesgo"])
            break
        except Exception:
            print("documento no valido")
    print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
    ff= input("ingrese el estado a colocar al estudiante")
    nte[car][doc]["riesgo"] = ff
    contenido = json.dumps(nte, indent=4)  
    with open("todos.json","w") as file:
            file.write(contenido)



def mod_fN():
    with open("todos.json") as file:
        nte = json.load(file)
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("seleccione uno de los cursos")
        print("U1","U2","U3","U4")
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
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
    print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
    print("escriba su documento a modificar(recuerde que tiene que estar en los documentos anteriores)")
    while True:
        try:
            doc = input("->")
            print("La nota final de ",nte[car][doc]["nombres"]," es ",nte[car][doc]["nota final"])
            break
        except Exception:
            print("documento no valido")
    fn = int(input("ingrese la nota que le quieres poner" ))
    nte[car][doc]["nota final"] = fn
    contenido = json.dumps(nte, indent=4)  
    with open("todos.json","w") as file:
        file.write(contenido)
    
    
def asig_tr():
    with open("trainer.json") as file:
        nte = json.load(file)
    st = ["1.el trainer", "2.el horario","3.la ruta","4. para salon"]
    srr = ["1.de 6 AM - 10 AM","2. de 10 AM - 2 PM","3. de 2 PM - 6 PM","4. de 6 PM - 10 PM"]
    frr = ["1. para la ruta NodeJS","2. para la ruta Java","3. para la ruta NetCore"]
    last = ["1.para poner a juan Marino como trainer","2.para poner a karen Regarla como trainer","3.para poner a Alma Marcela como trainer","4.para poner a Jorge Melo como trainer"]
   # print("seleccione uno de los cursos")
   #print("U1","U2","U3","U4")
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("seleccione uno de los cursos")
        print("U1","U2","U3","U4")
        
        try:
            car = input("....")
            for i in nte[car].values():
                print(i)
            break
        except Exception:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("codigo no valido")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("deseas cambiar ")
        for i in st:
            print(i)
        try:
            gg = int(input(" elige -> "))
            if gg == 1:
                print("para cambiar el trainer de ",car)
                for i in last:
                    print(i)
                opc = int(input("-> "))
                if opc == 1:
                    nte[car]["trainer"] = "juan Marino"
                elif opc == 2:
                    nte[car]["trainer"] = "karen Regarla"
                elif opc == 3:
                    nte[car]["trainer"] = "Alma Marcela"
                elif opc == 4:
                    nte[car]["trainer"] = "Jorge Melo"
                else:
                    print("no existe")
            elif gg == 2:
                print("para cambiar el horario de ",car)
                for i in srr:
                    print(i)
                kk = int(input("->"))
                if kk == 1:
                    nte[car]["horario"] = "de 6 AM - 10 AM"
                elif kk == 2:
                    nte[car]["horario"] = "de 10 AM - 2 PM"
                elif kk == 3:
                    nte[car]["horario"] = "de 2 PM - 6 PM"
                elif kk == 4:
                    nte[car]["horario"] = "de 6 PM - 10 PM"
                else:
                    print("no existe")
            elif gg == 3:
                print("para cambiar el horario de ",car)
                for i in frr:
                    print(i)
                jk = int(input("->"))
                if jk == 1:
                    nte[car]["ruta"] = "ruta NodeJS"
                elif jk == 2:
                    nte[car]["ruta"] = "ruta Java"
                elif jk == 3:
                    nte[car]["ruta"] = "ruta NetCore"
                else:
                    print("no existe")
            elif gg == 4:
                fr =["1,salon sputnik","2. salon artemis","3. salon apolo"]
                print("elige el salon que quieres que tenga ", car)
                for i in fr:
                    print(i)
                oi = int(input("ingrese el codigo del salon->"))
                if oi == 1:
                    nte[car]["salon"] = "sputnik"
                elif oi == 2:
                    nte[car]["salon"] = "artemis"
                elif oi == 3:
                    nte[car]["salon"] = "apolo"
            else:
                print("no existe")
        except Exception:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("no valido")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        n = input("deseas continuar marca si, si no marca enter")
        if n == "":
            break
    contenido = json.dumps(nte ,indent=4)
    with open("trainer.json","w") as file:
        file.write(contenido)
        
        
def muve():
    with open("todos.json") as file:
        nte = json.load(file)
    #print ("ingrese de donde quieres cambiar la persona")
    #print("U1  U2  U3  U4 registrados")
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print ("ingrese de donde quieres cambiar la persona")
        print("U1  U2  U3  U4 registrados")
        try:
            car = input("....")
            for i in nte[car]:
                print(i)
            break
        except Exception:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("no existe,recuerda que si es un salon la primera letra es en mayuscula")
            print("y el numero tiene que estar en el rango del curso")
            print("recuerda escribir bien registrados")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
    #print("escriba su documento a modificar(recuerde que tiene que estar en los documentos anteriores)")
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("escriba su documento a modificar(recuerde que tiene que estar en los documentos anteriores)")
        try:
            doc = input("->")
            print("escogiste a ",nte[car][doc]["apellidos"])
            break
        except Exception:
            print("documento no valido")
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("1. para cambiar o 2.para cancelar")
        inn = int(input("->"))
        if inn == 1 :
            gg = nte[car].pop(doc)
            while True:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("selecciona a donde lo quieres mover")
                print("U1  U2  U3  U4")
                try:
                    rac = input("....")
                    for i in nte[rac]:
                        print("wait....")
                    if len(nte[rac]) > 33:
                        nte[rac][doc] = gg
                        nte[rac][doc]["estado"] = "cursando"
                        print("exito")
                        break
                    else:
                        print("no hay cupo en este salon")    
                except Exception:
                    print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                    print("no existe,recuerda que si es un salon la primera letra es en mayuscula")
                    print("y el numero tiene que estar en el rango del curso")
                    print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")               
            contenido = json.dumps(nte, indent=4)
            with open("todos.json","w") as file:
                file.write(contenido)
            break
        else:
            break
                                     
                    
                               
                    







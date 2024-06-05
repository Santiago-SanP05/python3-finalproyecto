from registro import *

def regis():
    registrar()
    
    

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
            print("documento no valido")
                
    while True:
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("ingresa")
        for i in rr:
            print(i)
        try:
            inn = int(input("->"))
            if inn == 1:
                print(nte[car][doc]["notas 10"]," es su nota del 10 porciento")
                print(nte[car][doc]["notas 30"]," es su nota del 30 porciento")
                print(nte[car][doc]["notas 60"]," es su nota del 60 porciento")
                print(nte[car][doc]["nota final"]," es su nota final")
            elif inn == 2:
                print(print(nte[car][doc]["estado"]," es su estado"))
            elif inn == 3:
                print("su riesgo es :",nte[car][doc]["riesgo"])
            elif inn == 4:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("retrocediendo...")
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                break
        except Exception:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("no valido")  
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")    
        

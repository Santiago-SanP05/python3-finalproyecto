from funcoord import *
from funtrainer import *
from funcamp import *
import os

def menu():
    lista = ["1.Coordinador","2.Trainer","3.Camper","4.para salir"]

    while True:
        try:
            os.system('clear')
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("porfavor, ingrese la opccion a ingresar")
            for i in lista:
                print(i)
            try:
                ingresado = int(input("->"))
            except Exception:
                print("valor no valido -_-")
            if ingresado == 1:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("accediendo como coordinador")
                menu_coor()
            elif ingresado == 2:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("accediendo como Trainer")
                menu_tra()
            elif ingresado == 3:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("accediendo como Camper")
                menu_cam()
            elif ingresado == 4:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("Saliendo...")
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                break
            else:
                print("Error codigo no encontrado")
        except Exception:
            print("no valido piroba")
        
            
def menu_coor():
    while True:
        opc = ["1.para modificar el estado del estudiantes","2.para modificar el riesgo","3.modificar nota final","4 para reasignar trainer,ruta o horario","5.mover un estudiante","6. para salir"]
        os.system('clear')
        for i in opc:
            print(i)
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("ingrese su opccion")
        try:
            ingresado = int(input("->"))
            if ingresado == 1:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("Entrando...")
                mod_esta()
            elif ingresado == 2:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("Entrando...")
                mod_ries()
            elif ingresado == 3:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("Entrando...")
                mod_fN()
            elif ingresado == 4:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("Entrando...")
                asig_tr()
            elif ingresado == 5:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("entrando...")
                muve()
            elif ingresado == 6:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("fin")
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                break
        except Exception:
            print("valor no valido -_-")
def menu_tra():
    opc = ["1.para ingresar las notas","2. para asignar puntos","3. para retroceder"]
    while True:
        os.system('clear')
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("ingrese")
        for i in opc:
            print(i)
        try:
            ingr = int(input("->"))
            if ingr == 1:
                nota()
            elif ingr == 2:
                point()
            elif ingr == 3:
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                print("saliendo")
                print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
                break              
        except Exception:
            print("valor no valido -_-")
            
            
            
def menu_cam():
    opc = ["1.para registrarce","2.para ver como vas","cualquier otro para retroceder"]
    while True:
        os.system('clear')
        print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
        print("ingrese")
        for i in opc:
            print(i)
        try:
            ingr = int(input("->"))
        except Exception:
            print("valor no valido -_-")
        if ingr == 1:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("ingresando")
            regis()
        elif ingr == 2:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("ingresando")
            ver()
        else:
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            print("retrocediento...")
            print("⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇")
            break
            
            
            
            
            
            
            
            
        
        
        


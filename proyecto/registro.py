import json
mi = "todos.json"
grado = "registrados"
def registrar():
    with open(mi) as file:
        nte = json.load(file)
    estudiante={}
    while True:
        try:
            doc = int(input("Ingrese el documento: "))
            if nte[grado].get(doc,None) == None: 
                estudiante["nombres"] = input("ingrese sus nombres ->"),
                estudiante["apellidos"] = input("ingrese sus apellidos ->")
                estudiante["dcc"] = input("ingrese su direccion ->")
                estudiante["acudiente"] = input("su acudientes es ->")
                try:
                    estudiante["telefonos"] = int(input("ingrese su numero de telefono ->"))
                except Exception:
                    estudiante["telefonos"] = ""
                try:
                    estudiante["fijo"] = int(input("ingrese su numero fijo si no da enter ->"))
                except Exception:
                    estudiante["fijo"] = ""
                estudiante["estado"] = "inscrito"
                estudiante["riesgo"] = "bajo"
                estudiante["notas 60"] = 0
                estudiante["notas 30"] = 0
                estudiante["notas 10"] = 0
                estudiante["nota final"] = 0
                estudiante["point"] = 0
                nte[grado][doc] = estudiante
            else:
                print("documento ya existe mi pana")   
        except Exception:
            print("error al cargar")
        contenido = json.dumps(nte, indent=4)
        with open(mi,"w") as file:
            file.write(contenido)
        break









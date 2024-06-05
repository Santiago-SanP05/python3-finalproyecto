import json


with open("trainer.json") as file:
   nte = json.load(file)
   
rr = {}
rr = nte["U1"].pop("ruta")

print(type(rr))

maestres = {"Prioridad":4, "Descripcion":"maestre", "Personas":["Messi M","Cristiano C"]}
niños = {"Prioridad":2, "Descripcion":"niños", "Personas":["Mbappe M","Haaland H"]}
mecanicos = {"Prioridad":4, "Descripcion":"mecanicos", "Personas":["Ansu A","Pedri P"]}
mujeres = {"Prioridad":3, "Descripcion":"mujeres", "Personas":["Norma N","Valeria V"]}
ancianos = {"Prioridad":2, "Descripcion":"ancianos", "Personas":["Pele P","Maradona M"]}
niñas = {"Prioridad":1, "Descripcion":"niñas", "Personas":["Fatima F","Cassandra C"]}
hombre = {"Prioridad":3, "Descripcion":"hombre", "Personas":["Neymar N","Braithwaite B"]}
vigia = {"Prioridad":4, "Descripcion":"vigia", "Personas":["Lewandoski L","Iniesta I"]}
capitan = {"Prioridad":5, "Descripcion":"capitan", "Personas":["Xavi X","Benzema B"]}
timonel = {"Prioridad":4, "Descripcion":"timonel", "Personas":["Sergio S","Kevin K"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['Prioridad'], maestres)
cpa.enqueue(niños['Prioridad'], niños)
cpa.enqueue(mecanicos['Prioridad'], mecanicos)
cpa.enqueue(mujeres['Prioridad'], mujeres)
cpa.enqueue(ancianos['Prioridad'], ancianos)
cpa.enqueue(niñas['Prioridad'], niñas)
cpa.enqueue(hombre['Prioridad'], hombre)
cpa.enqueue(vigia['Prioridad'], vigia)
cpa.enqueue(capitan['Prioridad'], capitan)
cpa.enqueue(timonel['Prioridad'], timonel)

while not cpa.is_empty():
    cpa.to_string()
    sig = cpa.dequeue()
    print(f"Estos seran los siguientes en evacuar {sig}")
cpa.to_string()
print("Todo el barco ha sido evacuado")

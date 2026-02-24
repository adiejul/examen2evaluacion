



#creo el diccionario

listaTareas=["estudiar python", "hacer ejercicio", "leer 10 paginas"]
n=len(listaTareas)
tareas={}
for i in range (n):
    for j in listaTareas:
        tareas[j]= False



# def agregar_tareas(tareaNueva):

    

def marcar_hecha(tarea):
    if tarea in tareas:
        tareas[tarea] = True
    else:
        return "La tarea no existe"

def listar_tareas():
    for i in tareas:
        if tareas[i] == True:
            print ("[x]",i)
        else:
            print("[]",i)
    return ""

def contar_pendientes():
    cont =0
    for i in tareas:
        if tareas[i] == False:
            cont = cont +1
    if cont >1:
        return (f"Hay un total de {cont} tareas pendientes")
    elif cont ==1:
        return (f"Hay un total de {cont} tarea pendientes")
    else:
        return "No hay tareas pendientes"

if __name__=="__main__":
    
    print(listar_tareas())
    #agregar_tareas("sacar la basura")
    print("")
    marcar_hecha("estudiar python")
    print(listar_tareas())
    print(contar_pendientes())





    
    # agregar_tareas("barrer", "False")

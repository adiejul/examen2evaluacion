



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
    return "Aqui esta el listado de tus tareas"

def contar_pendientes():
    for i in tareas:
        cont =0
        if tareas[i] == False:
            cont = cont+1
        
    return cont

if __name__=="__main__":
    
    #Aqui creo el diccionario con la lista de tareas que pide el ejercicio:
    print("voy a listar las tareas")
    print("")
    print(listar_tareas())
    print("voy a agregar Sacar la basura")
    print("")
    #agregar_tareas("sacar la basura")
    print("marco como hecha estudiar python")
    print("")
    marcar_hecha("estudiar python")
    print("voy a listar las tareas")
    print("")
    print(listar_tareas())




    
    # agregar_tareas("barrer", "False")

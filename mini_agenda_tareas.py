
def agregar_tareas(tareaNueva, titulo):
    d


def marcar_hecha(tareas,titulo):
    for i in tareas:
        if i == titulo:
            tareas[i]==True
        else:
            return "La tarea no existe"

def listar_tareas(tareas):
    for i in tareas:
        if titulo[i] == True:
            print ("[x]",i)
        else:
            print("[]",i)

def contar_pendientes(tareas):
    for i in tareas:
        cont =0
        if diccionario[i]==False:
            cont = cont+1
        
    return cont
  



if __name__=="__main__":
    tareas=["estudiar python", "hacer ejercicio", "leer 10 paginas"]
    n=len(tareas)

    diccionario={}
    for i in tareas:
        diccionario=tareas[i]
        diccionario[i]= False

    print (diccionario)

    
    

'''
    agregar_tareas("barrer", "no hecha")

'''
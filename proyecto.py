nombre_proyecto = 'sistema de biblioteca'                   
descripcion  =  'permite gestionar libros, usuarios y préstamos en una biblioteca'                 
tecnologias = ['Python', 'Django', 'SQLite']                    
integrantes =['Juan Pérez', 'María Gómez', 'Carlos Rodríguez']                 
funcionalidades =['Registro de libros', 'Gestión de usuarios', 'Gestión de préstamos', 'Búsqueda de libros']                  

def mostrar_informacion():
    print(f"Nombre del proyecto: {nombre_proyecto}")
    print(f"Descripción: {descripcion}")
    print("Tecnologías utilizadas:")
    for tecnologia in tecnologias:
        print(f"- {tecnologia}")
    print("Integrantes del equipo:")
    for integrante in integrantes:
        print(f"- {integrante}")
    print("Funcionalidades principales:")
    for funcionalidad in funcionalidades:
        print(f"- {funcionalidad}")

mostrar_informacion()        
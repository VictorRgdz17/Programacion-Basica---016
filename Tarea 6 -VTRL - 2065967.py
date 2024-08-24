from datetime import datetime
from typing import List, Dict, Set, Union

# Tupla para la fecha (inmutable)
Fecha = Tuple[int, int, int, int, int, int]

class Tarea:
    def __init__(self, nombre: str, categoria: str, etiquetas: Set[str]):
        self.nombre = nombre
        self.categoria = categoria
        self.etiquetas = etiquetas
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        etiquetas = ", ".join(self.etiquetas)
        return f"Tarea: {self.nombre} | Categoría: {self.categoria} | Etiquetas: {etiquetas} | Fecha de creación: {self.fecha_creacion}"

class TareaConFechaLimite(Tarea):
    def __init__(self, nombre: str, categoria: str, etiquetas: Set[str], fecha_limite: Fecha):
        super().__init__(nombre, categoria, etiquetas)
        self.fecha_limite = datetime(*fecha_limite).strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"{super().__str__()} | Fecha límite: {self.fecha_limite}"

def agregar_tarea(tareas: List[Tarea], categorias: Dict[str, List[Tarea]]) -> None:
    nombre = input("Ingrese el nombre de la tarea: ")
    categoria = input("Ingrese la categoría de la tarea: ")
    etiquetas = set(input("Ingrese etiquetas separadas por coma: ").split(","))
    
    tarea = Tarea(nombre, categoria, etiquetas)
    tareas.append(tarea)
    
    if categoria not in categorias:
        categorias[categoria] = []
    categorias[categoria].append(tarea)
    
    print(f"Tarea '{nombre}' agregada.")

def mostrar_tareas(tareas: List[Tarea]) -> None:
    if not tareas:
        print("No hay tareas.")
    else:
        print("\nTareas:")
        for tarea in tareas:
            print(tarea)

def eliminar_tarea(tareas: List[Tarea]) -> None:
    if not tareas:
        print("No hay tareas para eliminar.")
        return

    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada.nombre}' eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

def modificar_tarea(tareas: List[Tarea]) -> None:
    if not tareas:
        print("No hay tareas para modificar.")
        return

    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea a modificar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea = tareas[indice]
            print(f"Modificando '{tarea.nombre}'")
            nombre = input(f"Nuevo nombre (actual: {tarea.nombre}): ")
            categoria = input(f"Nueva categoría (actual: {tarea.categoria}): ")
            etiquetas = set(input("Nuevas etiquetas separadas por coma: ").split(","))
            tarea.nombre = nombre
            tarea.categoria = categoria
            tarea.etiquetas = etiquetas
            print("Tarea modificada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

def gestor_de_tareas() -> None:
    tareas: List[Tarea] = []
    categorias: Dict[str, List[Tarea]] = {}
    
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Modificar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea(tareas, categorias)
        elif opcion == '2':
            mostrar_tareas(tareas)
        elif opcion == '3':
            eliminar_tarea(tareas)
        elif opcion == '4':
            modificar_tarea(tareas)
        elif opcion == '5':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    gestor_de_tareas()
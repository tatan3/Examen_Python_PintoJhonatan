from controllers import (
    menuprincipal
)
from utils import(
    generadores,
    terminal,
)
import json
from pathlib import Path

RUTA_DATOS = Path(__file__).parent.parent / "data/hamburgesas.json"

def cargar_datos():
    try:
        with open(RUTA_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(datos):
    with open(RUTA_DATOS, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2)

def menu_hamburgesas():
    while True:
        terminal.limpiar_pantalla()
        print('======== GESTOR DE HAMBURGESAS ========')
        print('1. NUEVA HAMBURGESA')
        print('2. ELIMINAR HAMBURGESA')
        print('3. LISTAR HAMBURGESAS')
        print('4. REGRESAR..........')
        try: 
            data = cargar_datos()
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            match opcion:
                case '1':
                    nombre = input("Nombre: ").strip()
                    categoria = input("Categoria: ").strip()                    
                    ingredientes = input("Ingredientes: ").strip()
                    precio = input("Precio: ").strip() 
                    chef = input("Chef: ").strip()                   
                    
                    nuevo_elemento = {
                        'id': generadores.generar_id(),
                        'Nombre': nombre,
                        'Categoria': categoria,
                        'Ingredientes': ingredientes,
                        'Precio':precio,
                        'Chef':chef
                    }
                    data.append(nuevo_elemento)
                    guardar_datos(data)
                    print(f"agregado con éxito! ID: {nuevo_elemento['id']}")
                    terminal.pausar()
                case '2':
                    datos = cargar_datos()
                    terminal.limpiar_pantalla()
                    terminal.mostrar_encabezado("ELIMINAR ELEMENTO")
                    
                    id_eliminar = input("Ingrese el ID del elemento a eliminar: ").strip()
                    nuevos_datos = [item for item in datos if item['id'] != id_eliminar]
                    
                    if len(nuevos_datos) == len(datos):
                        print("\nError: ID no encontrado")
                    else:
                        guardar_datos(nuevos_datos)
                        print("\n¡Elemento eliminado exitosamente!")
                    terminal.pausar()
                    return menu_hamburgesas()
                case '3':
                    data = cargar_datos()
                    terminal.limpiar_pantalla()
                    terminal.mostrar_encabezado("LISTA DE ELEMENTOS")
                    
                    if not data:
                        print("No hay elementos para mostrar.")
                    else:
                        tabla = []
                        for item in data:
                            tabla.append([
                                item['id'],
                                item['Nombre'],
                                item['Categoria'],
                                item['Ingredientes'],
                                item['Chef']

                            ])
                        terminal.mostrar_tabla(tabla, ["ID","Nombre","Categoria", "Ingredientes", "Chef"])
                    
                    terminal.pausar()
                    return menu_hamburgesas()
                case _:
                    terminal.limpiar_pantalla()
                    print('Retornando.......')
                    terminal.pausar()
            return menuprincipal.main_menu()
        except Exception:
            pass  
        
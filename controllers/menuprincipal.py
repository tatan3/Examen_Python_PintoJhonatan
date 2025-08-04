import controllers.menu_ingredientes as ingredientes
import controllers.menu_categorias as categorias
import utils.terminal as control

def main_menu():
    while True:
        control.limpiar_pantalla()
        print('======== MENU PRINCIPAL ========')
        print('1. GESTOR DE INGREDIENTES')
        print('2. GESTOR DE CATEGORIAS')
        print('3. GESTOR DE CHEFS')
        print('4. GESTOR DE HAMBURGESAS')
        print('5. MODULO DE REPORTES')
        print('6. SALIR')
        try:
            opcion =(input('Ingrese una opcion del 1 al 6: '))       
            match opcion:
                case '1':
                    ingredientes.menu_ingredientes()
                case '2':
                    categorias.menu_categorias()
                case _:
                    control.limpiar_pantalla()
                    print('Fuera de rango....')
                    control.pausar()
                    return main_menu()
        except ValueError:
            pass
    """"
        acciones = {
                '1': menu_ingredientes,
                '2':
                '3': 
                '4': 
                '5': 
                '6':
                '7': 
                '8': lambda: True
            }
    """
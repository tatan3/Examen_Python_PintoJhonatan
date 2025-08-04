import controllers.menu_ingredientes as ingredientes
import controllers.menu_categorias as categorias
import controllers.menu_chefs as chefs
import controllers.menu_hamburgesas as hamburgesa

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
                case '3':
                    chefs.menu_chefs()
                case '4':
                    hamburgesa.menu_hamburgesas()
                case _:
                    control.limpiar_pantalla()
                    print('Hasta pronto.......')
                    break
        except ValueError:
            pass
    
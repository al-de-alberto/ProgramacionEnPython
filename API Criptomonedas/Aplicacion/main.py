import time
from menus import menu, cryptos, agregar_registro, database
from utils import clear_screen, pausa
from conexion import bitcoin_database, ethereum_database, dogecoin_database, tether_database, chainlink_database, eliminar_database_info,listar_database_info
from api import bitcoin, ethereum, dogecoin, tether, chainlink

#https://www.coingecko.com/es

while True:
    clear_screen()
    menu()
    try:
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            while True:
                clear_screen()
                cryptos()
                try:
                    opcion = int(input('Ingrese una opcion: '))
                    if opcion == 1:
                        bitcoin()
                        pausa()
                    elif opcion == 2:
                        ethereum()
                        pausa()
                    elif opcion == 3:
                        dogecoin()
                        pausa()
                    elif opcion == 4:
                        tether()
                        pausa()
                    elif opcion == 5:
                        chainlink()
                        pausa()
                    elif opcion == 6:
                        print('Volviendo al menu principal...')
                        time.sleep(1.5)
                        break
                    else:
                        print('Opcion erronea. Reintente')
                        pausa()
                except:
                    print('Opcion erronea. Reintente')
                    pausa()
        elif opcion == 2:
            while True:
                clear_screen()
                database()
                try:
                    opcion = int(input('Ingrese una opcion: '))
                    if opcion == 1:
                        while True:
                            clear_screen()
                            agregar_registro()
                            try:
                                opcion = int(input('Ingrese una opcion: '))
                                if opcion == 1:
                                    bitcoin_database()
                                    pausa()
                                elif opcion == 2:
                                    ethereum_database()
                                    pausa()
                                elif opcion == 3:
                                    dogecoin_database()
                                    pausa()
                                elif opcion == 4:
                                    tether_database()
                                    pausa()
                                elif opcion == 5:
                                    chainlink_database()
                                    pausa()
                                elif opcion == 6:
                                    print('Volviendo al menu anterior...')
                                    time.sleep(1.5)
                                    break
                            except:
                                print('Opcion erronea. Reintente')
                                pausa()
                    elif opcion == 2: 
                        eliminar_database_info()
                        pausa()
                    elif opcion == 3:
                        listar_database_info()
                        pausa()
                    elif opcion == 4:
                        print('Volviendo al menu principal...')
                        time.sleep(1.5)
                        break
                except:
                    print('Opcion erronea. Reintente')
                    pausa()
        elif opcion == 3:
            print('Saliendo...')
            time.sleep(1.5)
            break
    except:
        print('Opcion erronea. Reintente')
        pausa()
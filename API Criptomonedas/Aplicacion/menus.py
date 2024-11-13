import time
from utils import clear_screen

def menu():
    print('Cargando...')
    time.sleep(0.8)
    clear_screen()
    print('********** MENU PRINCIPAL **********')
    print('1. Mostrar valores \n2. Base de Datos \n3. Salir')

def cryptos():
    print('Cargando...')
    time.sleep(0.8)
    clear_screen()
    print('********** VALOR CRIPTOMONEDAS **********')
    print('1. Bitcoin \n2. Ethereum \n3. Dogecoin \n4. Tether \n5. Chainlink \n6. Menu principal')

def agregar_registro():
    print('Cargando...')
    time.sleep(0.8)
    clear_screen()
    print('********** AGREGAR REGISTRO CRIPTOMONEDAS **********')
    print('1. Bitcoin \n2. Ethereum \n3. Dogecoin \n4. Tether \n5. Chainlink \n6. Menu anterior')
    
def database():
    print('Cargando...')
    time.sleep(0.8)
    clear_screen()
    print('********** BASE DE DATOS **********')
    print('1. Guardar registro \n2. Borrar registro \n3. Listar registros \n4. Menu principal')
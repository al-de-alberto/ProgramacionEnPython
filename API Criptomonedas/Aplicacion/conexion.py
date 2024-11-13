import mysql.connector, time, requests
from utils import clear_screen, pausa
from datetime import datetime

def conectar_database():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port='3306',
            database='criptomonedas'
        )
        if conexion.is_connected():
            clear_screen()
            print('Conectando...')
            time.sleep(0.8)
            print('¡Conexión realizada con éxito!')
            time.sleep(1.5)
            return conexion
    except mysql.connector.Error:
        print('Error de conexión...')
        return None

def guardar_registro(conexion, nombre, valor):
    try:
        cursor = conexion.cursor()
        fecha = datetime.now().date()
        sql = "INSERT INTO criptos (NOMBRE, VALOR, FECHA) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, float(valor), fecha))
        conexion.commit()
        print(f'Registro de {nombre} guardado con éxito.')
    except mysql.connector.Error:
        print('Error al guardar el registro')
    finally:
        cursor.close()

def borrar_registro(conexion, id_registro):
    try:
        cursor = conexion.cursor()
        sql = 'DELETE FROM criptos WHERE ID = %s'
        cursor.execute(sql, (id_registro,))
        conexion.commit()

        if cursor.rowcount > 0:
            print(f'Registro con la ID {id_registro} eliminado con éxito')
        else:
            print(f'No se encontró el registro con la ID {id_registro}')
    except mysql.connector.Error as err:
        print(f'Error al eliminar el registro: {err}')
    finally:
        cursor.close()

def listar_registros(conexion):
    try:
        cursor = conexion.cursor()
        sql = 'SELECT * FROM criptos'
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print('------------------')
        for fila in resultados:
            print(f"ID: {fila[0]} \nNombre: {fila[1]} \nValor: {fila[2]} \nFecha: {fila[3]}")
            print('------------------')
    except:
        print('Error al listar los registros')
    finally:
        cursor.close()

def bitcoin_database():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_valor = data['bitcoin']['usd']

        conexion = conectar_database()
        if conexion:
            guardar_registro(conexion, 'Bitcoin', bitcoin_valor)
            conexion.close

def ethereum_database():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ethereum_valor = data['ethereum']['usd']

        conexion = conectar_database()
        if conexion:
            guardar_registro(conexion, 'Ethereum', ethereum_valor)
            conexion.close

def dogecoin_database():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dogecoin_valor = data['dogecoin']['usd']

        conexion = conectar_database()
        if conexion:
            guardar_registro(conexion, 'Dogecoin', dogecoin_valor)
            conexion.close

def tether_database():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tether_valor = data['tether']['usd']

        conexion = conectar_database()
        if conexion:
            guardar_registro(conexion, 'Tether', tether_valor)
            conexion.close

def chainlink_database():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,chainlink&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        chainlink_valor = data['chainlink']['usd']

        conexion = conectar_database()
        if conexion:
            guardar_registro(conexion, 'Chainlink', chainlink_valor)
            conexion.close

def eliminar_database_info():
    id_registro = int(input('Ingrese el ID del registro a eliminar: '))
    conexion = conectar_database()
    if conexion:
        borrar_registro(conexion, id_registro)
        conexion.close()

def listar_database_info():
    conexion = conectar_database()
    if conexion:
        listar_registros(conexion)
        conexion.close()
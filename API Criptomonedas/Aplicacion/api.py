import requests
from datetime import datetime

def bitcoin():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_valor = data['bitcoin']['usd']
        print(f"El valor de Bitcoin del día {datetime.now().strftime('%d-%m-%Y')} es: ${bitcoin_valor}")

def ethereum():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ethereum_valor = data['ethereum']['usd']
        print(f"El valor de Ethereum del día {datetime.now().strftime('%d-%m-%Y')} es: ${ethereum_valor}")

def dogecoin():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dogecoin_valor = data['dogecoin']['usd']
        print(f"El valor de Dogecoin del día {datetime.now().strftime('%d-%m-%Y')} es: ${dogecoin_valor}")

def tether():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,solana&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tether_valor = data['tether']['usd']
        print(f"El valor de Tether del día {datetime.now().strftime('%d-%m-%Y')} es: ${tether_valor}")

def chainlink():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether,chainlink&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        chainlink_valor = data['chainlink']['usd']
        print(f"El valor de Chainlink del día {datetime.now().strftime('%d-%m-%Y')} es: ${chainlink_valor}")
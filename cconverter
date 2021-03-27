import requests


CHECKING_CACHE = 'Checking the cache...'
IN_CACHE = 'Oh! It is in the cache!'
NOT_IN_CACHE = 'Sorry, but it is not in the cache!'

currency_code = input().lower()
url = f'http://www.floatrates.com/daily/{currency_code}.json'
r = requests.get(url).json()
dct_currencies = {}

if currency_code != 'usd':
    dct_currencies['usd'] = float(r['usd']['rate'])
if currency_code != 'eur':
    dct_currencies['eur'] = float(r['eur']['rate'])


while True:
    received_code = input().lower()
    if received_code == '':
        break
    amount = int(input())
    print(CHECKING_CACHE)
    received_rate = float(r[received_code]['rate'])
    if received_code in dct_currencies.keys():
        print(IN_CACHE)
    else:
        print(NOT_IN_CACHE)
        dct_currencies[received_code] = received_rate
    result = round(amount * received_rate, 2)
    print(f'You received {result} {received_code.upper()}.')

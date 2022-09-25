from binance.client import Client

# Retrieve key and secret through either a txtfile or input into terminal
try:
    a = open('api_key.txt', 'r')
    api_key = a.read().strip()
except IOError:
    api_key = input('API Key:')
try:
    b = open('api_secret.txt', 'r')
    api_secret = b.read().strip()
except IOError:
    api_secret = input('API secret:')

# Launching the binance api client

client = Client(api_key, api_secret)
print('Successful login')



import requests
from hashlib import sha256

def get_price(ticker):
    """ acquire current price of stock from the IEX Cloud API """
    endpoint = "https://cloud.iexapis.com/stable/stock/{}/quote?token=".format(ticker)
    token = "sk_6e5dcfbafe9848d8971f95f2a5b2e90a"
    response = requests.get(endpoint + token).json()
    return response['latestPrice']

# def hash_password(password):
#     """ converts a plain-text password to a sha256 hashed version, 
#     for database storage and lookup """
#     return password

print(get_price('fb'))
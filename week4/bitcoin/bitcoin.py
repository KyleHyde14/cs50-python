import requests
import sys
# Changed API KEY after submition
URL = 'https://rest.coincap.io/v3/assets/bitcoin?apiKey=66df1b033a9a75fc88f0ee12e197c2a744075e014bdeff6665bec723aed437a3'

def main():
    multiplier = get_float()
    try:
        response = requests.get(URL).json()
        price = float(response['data']['priceUsd'])
    except (requests.RequestException, TypeError):
        sys.exit('Something went wrong')

    amount = multiplier * price
    
    print(f'${amount:,.4f}')
    return ''


def get_float():
    args = sys.argv
    if len(args) <= 1:
        sys.exit('Missing comand-line argument')
    
    try:
        num = float(args[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

    return num

if __name__ == '__main__':
    print(main())


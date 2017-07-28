import argparse
import urllib.request
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument('currency', help='Name of cryptocurrency, all lowercase')
args = parser.parse_args()
api_endpoint = 'https://api.coinmarketcap.com/v1/ticker/'
print('='*17)
print('= CRYPTOchecker =')
print('='*17)
response = urllib.request.urlopen(api_endpoint + args.currency).read()
print('LOADING DETAILS.  ', end='\r')
time.sleep(0.1)
print('LOADING DETAILS . ', end='\r')
time.sleep(0.1)
print('LOADING DETAILS  .', end='\r')
time.sleep(0.1)
print('LOADING DETAILS . ', end='\r')
time.sleep(0.1)
print('LOADING DETAILS.  ', end='\r')

json = json.loads(response)

print(json)

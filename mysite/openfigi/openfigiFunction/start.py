import requests     
import json         
import pandas as pd 
import pprint



tickers = ['ADS', 'BAS', 'DTE', 'SAP', 'SIE'] # Adidas, BASF, Deutsche Telekom, SAP & Siemens 

# jobs = [
#     {'idType': 'ID_CUSIP', 'idValue': '791642AA9'},
#     # {'idType': 'TICKER', 'idValue': 'BAS', 'micCode': 'XETR'},    
#     # {'idType': 'TICKER', 'idValue': 'DTE', 'micCode': 'XETR'},
#     # {'idType': 'TICKER', 'idValue': 'SAP', 'micCode': 'XETR'},
#     # {'idType': 'TICKER', 'idValue': 'SIE', 'micCode': 'XETR'}
# ]
# jobs.pop(0)
openfigi_apikey = ''  # Please put your own API Key here
openfigi_url = 'https://api.openfigi.com/v2/mapping'
openfigi_headers = {'Content-Type': 'text/json'}
idType= {}

def map_jobs(cusip_code):
    jobs = []
    idType ['idType']='ID_CUSIP'
    idType ['idValue']=cusip_code
    
    jobs.append(idType)


    if openfigi_apikey:
        openfigi_headers['X-OPENFIGI-APIKEY'] = openfigi_apikey
    response = requests.post(url=openfigi_url, headers=openfigi_headers,
                             json=jobs)
    if response.status_code != 200:
        del jobs
        raise Exception('Bad response code {}'.format(str(response.status_code)))
    del jobs
    return response.json()

from pip._vendor.distlib.compat import raw_input
import json
import requests

def accessOMIM():
    url = 'http://api.omim.org/api/entry?mimNumber=100100'
    apikey = 'gZuFDYrRTlKEPLkePeEBog'
    r = requests.get(url)
    r.status_code

def inputUser():
    geneSymbol = raw_input('Enter approved gene symbol of interest:')
 
    
inputUser()

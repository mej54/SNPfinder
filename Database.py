from pip._vendor.distlib.compat import raw_input
import json
import urllib2

def accessOMIM(query):
    gene = query
    url = 'https://api.omim.org/api/entry/search?search='
    #https://api.omim.org/api/entry/search?search=pik3ca&filter=&fields=&retrieve=&start=0&limit=10&sort=&operator=&include=allelicVariantList&include=clinicalSynopsis&format=json
    filters = '&filter=&fields=&retrieve=&start=0&limit=10&sort=&operator=&include=allelicVariantList&include=clinicalSynopsis&format=json' 
    apikey = '&apiKey=gZuFDYrRTlKEPLkePeEBog'
    final_url = url + gene + filters + apikey
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    print data

def inputUser():
    geneSymbol = raw_input('Enter approved gene symbol of interest:')
    accessOMIM(geneSymbol)
    
inputUser()

#!/usr/bin/env python3
import requests

url = "https://query.wikidata.org/sparql"

query = '''
SELECT ?country ?countryLabel ?capitalLabel WHERE {
    ?country wdt:P36 ?capital .
    ?country wdt:P31 wd:Q6256 .

    SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
    }
}'''

data = requests.get(url, params={'query': query, 'format': 'json'}).json()

for item in data['results']['bindings']:
    country = item['countryLabel']['value']
    capital = item['capitalLabel']['value']
    print('{}\t{}'.format(country, capital))

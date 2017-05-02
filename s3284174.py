#!/usr/bin/env python3

# Simple QA project
# Language Technology
# (BA) Information Science - University of Groningen
# Leon Wetzel (l.f.a.wetzel@student.rug.nl)

import argparse

import requests

# Retrieve query number
parser = argparse.ArgumentParser()
parser.add_argument("ID", type=int)
args = parser.parse_args()

# Assign URL
url = "https://query.wikidata.org/sparql"

# Execute query based on argument
# TODO: make dynamic?
if args.ID == 1:
    # NOTE:
    # Question has been altered, since it was difficult to answer the rather open question
    # 'What is tiramisu?'.
    question = "What are typical Italian desserts?"

    query = '''
    SELECT ?foodLabel WHERE {
        ?food wdt:P279 wd:Q182940.
        ?food wdt:P495 wd:Q38.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['foodLabel']['value']
        print('{}'.format(answer))

elif args.ID == 2:
    question = "Which colours can an apple have?"

    query = '''
    SELECT DISTINCT ?colorLabel WHERE {
        ?item wdt:P31/wdt:P279* wd:Q89 ;
        wdt:P462 ?color ;
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['colorLabel']['value']
        print('{}'.format(answer))

elif args.ID == 3:
    question = "What is the scientific name of pear?"

    query = '''
    SELECT ?itemLabel WHERE {
        wd:Q13099586 wdt:P1582 ?item
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['itemLabel']['value']
        print('{}'.format(answer))

elif args.ID == 4:
    question = "Which material is used for producing dog food?"

    query = '''
    SELECT ?itemLabel WHERE {
        wd:Q38420 wdt:P186 ?item.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['itemLabel']['value']
        print('{}'.format(answer))

elif args.ID == 5:
    question = "How is honey produced?"

    query = '''
    SELECT ?itemLabel WHERE {
        wd:Q10987 wdt:P2079 ?item.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['itemLabel']['value']
        print('{}'.format(answer))

elif args.ID == 6:
    # NOTE:
    # Wikidata considers cucumber as a subclass of both fruit and vegetable!
    # The description says: 'fruit used as vegetable'
    question = "Is cucumber considered fruit or vegetable?"

    query = '''        
        SELECT ?label WHERE { wd:Q2735883 schema:description ?label.
            FILTER(LANG(?label) = "en")
        }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['label']['value']
        print('{}'.format(answer))

elif args.ID == 7:
    question = "Which nut causes peanut allergy?"

    query = '''
        SELECT ?itemLabel WHERE {
            wd:Q7157933 wdt:P828 ?item.
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['itemLabel']['value']
        print('{}'.format(answer))

elif args.ID == 8:
    question = "What is bouillon?"

    query = '''
        SELECT ?label WHERE { wd:Q4949468 schema:description ?label.
            FILTER(LANG(?label) = "en")
        }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['label']['value']
        print('{}'.format(answer))

elif args.ID == 9:
    question = "Where does pasta come from?"

    query = '''
        SELECT ?itemLabel WHERE {
            wd:Q178 wdt:P495 ?item.
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['itemLabel']['value']
        print('{}'.format(answer))

elif args.ID == 10:
    question = "Of which ingredients does apple pie consist?"
    query = '''
        SELECT ?itemLabel WHERE {
            wd:Q1068034 wdt:P527 ?item.
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    print(question)
    for item in data['results']['bindings']:
        answer = item['itemLabel']['value']
        print('{}'.format(answer))
else:
    print("Unable to execute query.")

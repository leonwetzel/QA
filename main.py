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
if args.ID == 1:
    question = "What is tiramisu?"

    query = '''
    SELECT ?countryLabel ?capitalLabel WHERE {
        ?country wdt:P36 ?capital .
        ?country wdt:P31 wd:Q6256 .

        SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en" .
        }
    }'''

    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    for item in data['results']['bindings']:
        answer = item['countryLabel']['value']
        print('{}\n{}'.format(question, answer))

elif args.ID == 2:
    question = "Which colours can an apple have?"
    print("ham")
elif args.ID == 3:
    question = "What is the scientific name of pear?"
    print("jam")
elif args.ID == 4:
    question = "Which material is used for producing dog food?"
    print("ham")
elif args.ID == 5:
    question = "How is honey produced?"
    print("jam")
elif args.ID == 6:
    question = "Is cucumber considered fruit or vegetable?"
    print("ham")
elif args.ID == 7:
    question = "Which nut causes peanut allergy?"
    print("jam")
elif args.ID == 8:
    question = "What is bouillon?"
    print("jam")
elif args.ID == 9:
    question = "Where does pasta come from?"
    print("ham")
elif args.ID == 10:
    question = "Of which ingredients does apple pie consist?"
    print("jam")
else:
    print("Unable to execute query.")

query = '''
SELECT ?countryLabel ?capitalLabel WHERE {
    ?country wdt:P36 ?capital .
    ?country wdt:P31 wd:Q6256 .

    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "en" .
    }
}'''

data = requests.get(url, params={'query': query, 'format': 'json'}).json()

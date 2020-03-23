#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
import json
import re

ministerium_url = "https://info.gesundheitsministerium.at/data/"

simpledata_query = "SimpleData"

queries = ['Geschlechtsverteilung', 'Altersverteilung', 'Bezirke', 'Bundesland']

output = {}

def get_data(query):
    text = urlopen(ministerium_url + query + '.js').read().decode('utf-8').rstrip()
    json_text = re.search(r'^var.*\s*=\s*(\[\{.*?\}\])\s*;$', str(text), flags=re.DOTALL).group(1)
    return json.loads(json_text)

for x in queries:
    output[x] = get_data(x)

print(json.dumps(output,indent=2))


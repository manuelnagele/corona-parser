#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from geodatahelper import get_geodata_for_district
import json
import re

ministerium_url = "https://info.gesundheitsministerium.at/data/"

queries = ['Geschlechtsverteilung', 'Altersverteilung', 'Bezirke', 'Bundesland', 'SimpleData']


output = {}

def get_data(query):
    text = urlopen(ministerium_url + query + '.js').read().decode('utf-8')
    if query == 'SimpleData':
        data = []
        simplematch = re.compile(r'^var\s(.*)\s=\s(\d.*);$')
        for line in text.split('\n'):
            try:
                data.append({"label":simplematch.search(line).group(1),"y":int(simplematch.search(line).group(2))})
            except:
                pass
        return data
    else:
        json_text = re.search(r'^var.*\s*=\s*(\[\{.*?\}\])\s*;$', str(text), flags=re.DOTALL).group(1)
        data = json.loads(json_text)
      
        if query == 'Bezirke':
            for district in data:
                district.update(get_geodata_for_district(district['label']))
        return data

for x in queries:
    output[x] = get_data(x)

print(json.dumps(output,indent=2))

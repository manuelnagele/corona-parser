#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from geodatahelper import get_geodata_for_district
import json
import re

with open("./config.json") as config_file:
    config = json.load(config_file)

write_to_file = config['logging']['write_to_file']
file_location = config['logging']['file_location']
ministerium_url = config['datasource']['ministerium_url']
queries = config['datasource']['queries']

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
        
        for datapoint in data:
            datapoint['query'] = query
            if query == 'Bezirke':
                datapoint.update(get_geodata_for_district(datapoint['label']))
        return data

for x in queries:
    output[x] = get_data(x)

output = json.dumps(output, indent=2, ensure_ascii=False))

if write_to_file:
    with open(file_location, "w") as file:
        file.write(output)
else:
    print(output)
